from telethon import TelegramClient
from telethon.tl.types import MessageEntityUrl, MessageEntityTextUrl
import re
import asyncio

# 配置你的API认证信息
api_id = ''  # 请填写你的API ID
api_hash = ''  # 请填写你的API Hash
channel_username = ''  # 目标频道用户名

# 输出文件路径
OUTPUT_FILE = "telegraph_links.txt"

def extract_telegraph_links(message):
    """
    从消息中提取所有 Telegraph 图片链接，并过滤掉带括号的 URL。
    :param message: 消息对象
    :return: Telegraph 链接列表
    """
    links = []

    # 从消息实体中提取链接
    if message.entities:
        for entity in message.entities:
            if isinstance(entity, (MessageEntityUrl, MessageEntityTextUrl)):
                if isinstance(entity, MessageEntityUrl):
                    url = message.text[entity.offset:entity.offset + entity.length]
                else:
                    url = entity.url
                # 判断是否为 Telegraph 链接，并且不包含非法字符（如括号）
                if re.match(r'https?://(?:telegra\.ph|telegraph\.ph)/[^\s\)]+', url):
                    links.append(url)

    # 使用正则表达式从文本中提取 Telegraph 链接
    if message.text:
        telegraph_pattern = r'https?://(?:telegra\.ph|telegraph\.ph)/[^\s\)]+'
        links.extend(re.findall(telegraph_pattern, message.text))

    # 去重
    return list(set(links))

async def get_channel_messages():
    """
    获取频道消息并提取 Telegraph 链接。
    """
    async with TelegramClient('session_name', api_id, api_hash) as client:
        # 打开文件准备写入
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            # 获取频道的所有消息
            async for message in client.iter_messages(channel_username):
                # 提取 Telegraph 链接
                telegraph_links = extract_telegraph_links(message)

                # 如果有 Telegraph 链接，写入文件
                if telegraph_links:
                    for link in telegraph_links:
                        f.write(f"{link}\n")
                    print(f"Found {len(telegraph_links)} Telegraph links in message {message.id}")

        print(f"All Telegraph links have been saved to {OUTPUT_FILE}")

# 运行
if __name__ == "__main__":
    asyncio.run(get_channel_messages())
