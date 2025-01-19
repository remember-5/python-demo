import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from tqdm import tqdm
import aiofiles
from urllib.parse import urlparse
import yaml
from loguru import logger

# 加载配置文件
def load_config(config_file="config.yml"):
    with open(config_file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 配置日志系统
def setup_logging(log_file="telegraph_downloader.log", max_log_size=10, backup_count=5):
    """配置 loguru 日志系统，max_log_size 单位为 MB"""
    logger.add(
        log_file,
        rotation=f"{max_log_size} MB",  # 日志文件大小限制
        retention=f"{backup_count} days",  # 保留日志文件的天数
        encoding="utf-8",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}"
    )

async def download_image(session, url, save_dir, pbar, semaphore, max_retries):
    """异步下载单个图片，支持重试机制"""
    async with semaphore:
        retries = 0
        while retries < max_retries:
            try:
                # 处理 URL 格式
                full_url = f"https://telegra.ph{url}" if url.startswith('/') else url

                # 从 URL 中获取原始文件名
                filename = os.path.basename(urlparse(url).path)
                save_path = os.path.join(save_dir, filename)

                # 检查文件是否已存在
                if os.path.exists(save_path):
                    logger.debug(f"Skipped: {filename} (already exists)")
                    pbar.update(1)
                    return True

                async with session.get(full_url) as response:
                    if response.status == 200:
                        async with aiofiles.open(save_path, 'wb') as f:
                            await f.write(await response.read())
                        pbar.update(1)
                        return True
                    elif response.status == 500:
                        retries += 1
                        logger.warning(f"Retry {retries}/{max_retries}: Failed to download {filename} (HTTP 500)")
                        await asyncio.sleep(1)  # 等待 1 秒后重试
                    else:
                        logger.error(f"Failed to download {filename}: HTTP {response.status}")
                        return False
            except Exception as e:
                logger.error(f"Error downloading {filename}: {str(e)}")
                return False

        # 如果重试次数用完，记录失败
        logger.error(f"Failed to download {filename} after {max_retries} retries")
        return False

async def process_url(session, url, semaphore, download_base_path, max_retries):
    """处理单个 URL"""
    try:
        # 获取页面内容
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch page: {response.status}")
            html_content = await response.text()

        # 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 获取标题
        title = soup.find('h1').text.strip()
        # 清理标题中的非法字符
        title = ''.join(char if char not in '<>:"/\\|?*' else '_' for char in title)

        # 创建保存目录
        save_dir = os.path.join(download_base_path, title)
        os.makedirs(save_dir, exist_ok=True)

        # 获取 article 标签下的所有图片 URL
        article = soup.find('article')
        if not article:
            raise Exception("Article tag not found")

        img_urls = [img.get('src') for img in article.find_all('img')]
        # 过滤掉 None 和空字符串
        img_urls = [url for url in img_urls if url]

        if not img_urls:
            raise Exception("No images found in article")

        total_images = len(img_urls)
        logger.info(f"Starting download: {title}")
        logger.info(f"Total images found: {total_images}")

        # 创建进度条
        pbar = tqdm(total=total_images, desc="Downloading", unit="img")

        # 创建下载任务
        tasks = []
        for img_url in img_urls:
            task = download_image(session, img_url, save_dir, pbar, semaphore, max_retries)
            tasks.append(task)

        # 执行所有下载任务
        results = await asyncio.gather(*tasks)

        # 统计成功下载的文件数
        successful_downloads = sum(1 for result in results if result)

        pbar.close()

        # 验证下载完成后的文件数量
        actual_files = len([f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))])

        # 返回结果
        return {
            'url': url,
            'title': title,
            'total_images': total_images,
            'successful': successful_downloads,
            'actual_files': actual_files,
            'save_dir': save_dir
        }

    except Exception as e:
        logger.error(f"Error processing {url}: {str(e)}")
        return {
            'url': url,
            'error': str(e)
        }

async def process_urls(urls_file, semaphore, download_base_path, max_retries):
    """按顺序处理 URL 列表"""
    async with aiohttp.ClientSession() as session:
        with open(urls_file, "r", encoding="utf-8") as f:
            for line in f:
                url = line.strip()
                if not url:
                    continue

                logger.info(f"Processing URL: {url}")
                result = await process_url(session, url, semaphore, download_base_path, max_retries)

                # 处理结果
                if 'error' in result:
                    logger.error(f"Failed to process {url}: {result['error']}")
                else:
                    # 只在出现差异时显示警告
                    if result['actual_files'] != result['total_images']:
                        logger.warning(
                            f"File count mismatch: {result['actual_files']} files found, "
                            f"expected {result['total_images']}"
                        )

                    logger.info(
                        f"Completed: {result['successful']}/{result['total_images']} "
                        f"files saved to {result['save_dir']}"
                    )

async def main(config):
    # 创建信号量以控制并发数
    semaphore = asyncio.Semaphore(config["max_concurrent_downloads"])

    # 按顺序处理 URL
    await process_urls(config["urls_file"], semaphore, config["download_base_path"], config["max_retries"])

if __name__ == "__main__":
    # 加载配置文件
    config = load_config()

    # 配置日志系统
    setup_logging(
        log_file=config.get("log_file", "telegraph_downloader.log"),
        max_log_size=config.get("max_log_size", 10),  # 默认 10MB
        backup_count=config.get("log_backup_count", 5)  # 默认保留 5 个备份
    )

    # 确保下载目录存在
    os.makedirs(config["download_base_path"], exist_ok=True)

    # 运行主程序
    asyncio.run(main(config))
