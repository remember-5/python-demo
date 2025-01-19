import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from tqdm import tqdm
import aiofiles
from urllib.parse import urlparse
import logging
import yaml

# 加载配置文件
def load_config(config_file="config.yml"):
    with open(config_file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 加载下载链接
def load_urls(urls_file):
    with open(urls_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

async def download_image(session, url, save_dir, pbar, semaphore, max_retries):
    """异步下载单个图片，支持重试机制"""
    async with semaphore:
        retries = 0
        while retries < max_retries:
            try:
                # 处理URL格式
                full_url = f"https://telegra.ph{url}" if url.startswith('/') else url

                # 从URL中获取原始文件名
                filename = os.path.basename(urlparse(url).path)
                save_path = os.path.join(save_dir, filename)

                # 检查文件是否已存在
                if os.path.exists(save_path):
                    logging.debug(f"Skipped: {filename} (already exists)")
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
                        logging.warning(f"Retry {retries}/{max_retries}: Failed to download {filename} (HTTP 500)")
                        await asyncio.sleep(1)  # 等待1秒后重试
                    else:
                        logging.error(f"Failed to download {filename}: HTTP {response.status}")
                        return False
            except Exception as e:
                logging.error(f"Error downloading {filename}: {str(e)}")
                return False

        # 如果重试次数用完，记录失败
        logging.error(f"Failed to download {filename} after {max_retries} retries")
        return False

async def download_telegraph_images(url, semaphore, download_base_path, max_retries):
    """获取HTML内容并下载所有图片"""
    async with aiohttp.ClientSession() as session:
        # 获取页面内容
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch page: {response.status}")
            html_content = await response.text()

        # 解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 获取标题
        title = soup.find('h1').text.strip()
        # 清理标题中的非法字符
        title = ''.join(char if char not in '<>:"/\\|?*' else '_' for char in title)

        # 创建保存目录
        save_dir = os.path.join(download_base_path, title)
        os.makedirs(save_dir, exist_ok=True)

        # 获取article标签下的所有图片URL
        article = soup.find('article')
        if not article:
            raise Exception("Article tag not found")

        img_urls = [img.get('src') for img in article.find_all('img')]
        # 过滤掉None和空字符串
        img_urls = [url for url in img_urls if url]

        if not img_urls:
            raise Exception("No images found in article")

        total_images = len(img_urls)
        logging.info(f"Starting download: {title}")
        logging.info(f"Total images found: {total_images}")

        # 创建进度条
        pbar = tqdm(total=total_images, desc="Downloading", unit="img")

        # 创建下载任务
        tasks = []
        for url in img_urls:
            task = download_image(session, url, save_dir, pbar, semaphore, max_retries)
            tasks.append(task)

        # 执行所有下载任务
        results = await asyncio.gather(*tasks)

        # 统计成功下载的文件数
        successful_downloads = sum(1 for result in results if result)

        pbar.close()

        # 验证下载完成后的文件数量
        actual_files = len([f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))])

        return {
            'title': title,
            'total_images': total_images,
            'successful': successful_downloads,
            'actual_files': actual_files,
            'save_dir': save_dir
        }

async def main(config):
    # 加载下载链接
    telegraph_urls = load_urls(config["urls_file"])

    # 创建信号量以控制并发数
    semaphore = asyncio.Semaphore(config["max_concurrent_downloads"])

    # 创建下载任务
    tasks = [
        download_telegraph_images(url, semaphore, config["download_base_path"], config["max_retries"])
        for url in telegraph_urls
    ]

    # 执行所有下载任务
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # 处理结果
    for result in results:
        if isinstance(result, Exception):
            logging.error(f"Download failed: {str(result)}")
        else:
            # 只在出现差异时显示警告
            if result['actual_files'] != result['total_images']:
                logging.warning(
                    f"File count mismatch: {result['actual_files']} files found, "
                    f"expected {result['total_images']}"
                )

            logging.info(
                f"Download completed: {result['successful']}/{result['total_images']} "
                f"files saved to {result['save_dir']}"
            )

if __name__ == "__main__":
    # 加载配置文件
    config = load_config()

    # 确保下载目录存在
    os.makedirs(config["download_base_path"], exist_ok=True)

    # 运行主程序
    asyncio.run(main(config))
