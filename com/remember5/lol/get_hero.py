import json

import requests


def get_hero_list():
    """
    获取英雄信息
    """
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    res = requests.get(url)
    if res.status_code != 200:
        print('获取英雄信息失败')
        return None
    return res.json()


def download_hero_list():
    """
    保存所有英雄信息
    """
    hero_list = get_hero_list()
    with open(hero_list['fileTime'] + ' hero_list.json', 'w', encoding='utf-8') as f:
        json.dump(hero_list, f, indent=4, ensure_ascii=False)


def download_avatar(hero_name):
    """
    下载英雄头像
    Args:
        hero_name: 英雄名
    """
    url = 'https://game.gtimg.cn/images/lol/act/img/champion/{}.png'.format(hero_name)
    res = requests.get(url)
    if res.status_code != 200:
        print('下载头像失败')
    with open('avatar/{}.png'.format(hero_name), 'wb') as f:
        f.write(res.content)


def download_all_hero_avatars():
    """
    下载所有英雄头像
    """
    hero_list = get_hero_list()
    for hero in hero_list['hero']:
        download_avatar(hero['alias'])


def download_hero_info(hero_id, hero_name):
    """
    下载英雄信息
    Args:
        hero_id: 英雄id
        hero_name: 英雄名
    """
    url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(hero_id)
    res = requests.get(url)
    if res.status_code != 200:
        print('下载英雄信息失败')
    with open('hero_info/{}.json'.format(hero_name), 'wb') as f:
        f.write(res.content)


def download_all_hero_info():
    """
    下载所有英雄信息
    """
    hero_list = get_hero_list()
    for hero in hero_list['hero']:
        download_hero_info(hero['heroId'], hero['name'])


if __name__ == '__main__':
    download_hero_list()
    download_all_hero_avatars()
    download_all_hero_info()
