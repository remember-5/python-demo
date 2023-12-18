from sqlite3 import IntegrityError

import requests
import sqlite_utils

db = sqlite_utils.Database("kfc.db")


def mini_programs():
    url = "https://zy3-craze-thurs.87654.vip/api/index/getRandText"

    payload = {}
    headers = {
        'Host': 'zy3-craze-thurs.87654.vip',
        'referer': 'https://servicewechat.com/wx103724e0f6111659/1/page-frame.html',
        'xweb_xhr': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF XWEB/30626',
        'token': '',
        'content-type': 'application/json',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'zh-CN,zh'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        rep_json = response.json()
        if rep_json['code'] == 200:
            content = rep_json['data']['content']
            save(content)


def read_local_file():
    """
    读取本地文件
    """
    with open('content.txt', 'r') as file:
        for line in file:
            save(line.strip())


def github_1():
    """
    url https://github.com/whitescent/KFC-Crazy-Thursday
    """
    url = "https://raw.githubusercontent.com/Nthily/KFC-Crazy-Thursday/main/kfc.json"
    response = requests.get(url).json()
    for x in response:
        text = x['text']
        if text is not None:
            save(text)


def get_all_content():
    """
    获取所有文本信息
    """
    read_local_file()
    github_1()
    for _ in range(10):
        mini_programs()


def save(text):
    try:
        db["kfc"].insert({"text": text})
    except IntegrityError:
        print('已存在', text)


if __name__ == '__main__':
    if db["kfc"].exists() is False:
        db.execute("""
            create table kfc
                (
                    id   INTEGER not null
                        constraint kfc_pk
                            primary key autoincrement,
                    text TEXT    not null
                        constraint kfc_pk2
                            unique
                );
            """)
    get_all_content()
    db.close()
