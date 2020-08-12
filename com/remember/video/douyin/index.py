# coding:utf-8
import json
import os
import re

import time
import queue
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread

import requests
from urllib import parse

ies_url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/"  # ies地址

user_post = "https://www.iesdouyin.com/web/api/v2/aweme/post/"  # 用户作品
user_like = "https://www.iesdouyin.com/web/api/v2/aweme/like/"  # 用户喜欢
user_info_url = "https://www.iesdouyin.com/web/api/v2/user/info/"  # 用户详情

challenge_url = "https://www.iesdouyin.com/web/api/v2/challenge/aweme/"  # 挑战地址
challenge_info_url = "https://www.iesdouyin.com/web/api/v2/challenge/info/"  # 挑战详情

music_url = "https://www.iesdouyin.com/web/api/v2/music/list/aweme/"  # 音乐地址
music_info_url = "https://www.iesdouyin.com/web/api/v2/music/info/"  # 音乐详情

hd = {
    'authority': 'aweme.snssdk.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                  'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

THREADS = 2
# 每次分页数量
PAGE_NUM = 10

# TODO 后期增加多线程下载
# 10个线程
pool = ThreadPoolExecutor(10)

HEADERS = {
    'authority': 'aweme.snssdk.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'accept': 'application/json',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A372 Safari/604.1",
}


def get_dy_url_id(url, char="?"):
    return url.split(char)[0].split("/")[-1]


def generate_signature(uid):
    """
    生成_signature
    :param uid: id
    :return: _signature
    """
    # p = os.popen('node my.js %s' % uid)
    p = os.popen('node fuck-byted-acrawler.js %s' % uid)
    return p.readlines()[0].replace("\n", "")


def get_real_address(url):
    """
    获取真实地址
    :param url: 分享的url
    :return: 真实地址
    """
    if url.find('v.douyin.com') < 0:
        return url
    res = requests.get(url, headers=HEADERS, allow_redirects=False)
    return res.headers['location'] if res.status_code == 302 else None


def download(url=None, video_id=None, save_path=None):
    """
    下载视频
    :param url: 无水印播放地址
    :param video_id: video id
    :param save_path: 保存路径
    :return:
    """
    # TODO 后续增加保存路径
    current_folder = os.path.abspath(os.path.dirname(os.getcwd()))
    target_folder = os.path.join(current_folder, 'download/%s.mp4' % video_id)
    if not os.path.exists(target_folder):
        video_url = requests.get(url=url, headers=hd, allow_redirects=False).headers['location']

        print("开始下载", video_id)
        r = requests.get(video_url, stream=True)

        with open('../download/{}.mp4'.format(video_id), "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)

        print("下载结束", video_id)
    else:
        print("文件已经存在")


# 下载队列
class DownloadWorker(Thread):
    def __init__(self, _queue, thread_name):
        Thread.__init__(self, name=thread_name)
        print("DownloadWorker")
        self.queue = _queue

    def run(self):
        while True:
            print(self.name)
            # medium_type, uri, download_url, target_folder = self.queue.get()
            # download(medium_type, uri, download_url, target_folder)
            # self.queue.task_done()


class DouYinCrawler:
    def __init__(self, conf_path="url.txt"):
        """
        init
        :param conf_path: 配置文件位置
        """
        self.video = []  # 单个
        self.numbers = []  # 用户
        self.challenges = []  # 挑战
        self.musics = []  # 音乐

        for line in open(conf_path, 'r').readlines():
            url = get_real_address(line.strip('\n'))  # 去掉换行符
            if not url:
                continue
            if re.search('share/video', url):
                self.video.append(url)
            if re.search('share/user', url):
                self.numbers.append(url)
            if re.search('share/challenge', url):
                self.challenges.append(url)
            if re.search('share/music', url):
                self.musics.append(url)

        self.queue = queue.Queue(20)
        self.scheduling()

    def scheduling(self):
        """
        任务调度
        :return:
        """
        # for x in range(THREADS):
        #     worker = DownloadWorker(self.queue, thread_name="Thread-%s" % x)
        #     worker.daemon = True
        #     worker.start()

        # for url in self.video:
        #     self.download_share_videos(url)
        for url in self.numbers:
            self.download_user_videos(url)
        # for url in self.challenges:
        #     self.download_challenge_videos(url)
        # for url in self.musics:
        #     self.download_music_videos(url)
        return

    def download_share_videos(self, url):
        """
        下载用户分享视频
        :param url: 视频地址
        """
        # 从url中取出视频的id
        video_id = get_dy_url_id(url)

        data = requests.get(url=ies_url, params={"item_ids": video_id, "dytk": ""}).json()
        play_url = data['item_list'][0]['video']['play_addr']['url_list'][0].replace('playwm', "play")
        download(play_url, video_id)

    def download_user_videos(self, url, _max_cursor=0):
        """
        下载用户的视频，包括作品和喜欢
        :param url: 用户主页地址
        :param _max_cursor: 最大游标
        :return:
        """
        print("download_user_videos | url", url)

        # 获取sec_uid
        params = parse.parse_qs(parse.urlparse(url).query)
        sec_uid = params['sec_uid'][0]

        # 获取uid
        uid = get_dy_url_id(url)
        _signature = generate_signature(uid)

        self.download_user_post(sec_uid, _signature, _max_cursor)
        # self.download_user_like(sec_uid, _signature, _max_cursor)

    def download_user_post(self, sec_uid, _signature, _count=9, _max_cursor=0):
        """
        下载作品
        :param sec_uid:
        :param _signature:
        :param _count:
        :param _max_cursor:
        :return:
        """
        post_data = ''
        while True:
            content = requests.get(url=user_post, params={
                "sec_uid": str(sec_uid),
                "count": _count,
                "max_cursor": str(_max_cursor),
                "aid": 1128,
                "_signature": str(_signature),
                "dytk": "",
            }, allow_redirects=False).text.replace("\n", "")
            post_data = json.loads(content)
            print(post_data)
            if len(post_data['aweme_list']) > 0:
                break
            time.sleep(2)

        print("获取分页数据成功")
        max_cursor = post_data['max_cursor']
        print("最新_cursor", max_cursor)
        for x in post_data['aweme_list']:
            video_id = x['aweme_id']
            download(x['video']['play_addr']['url_list'][0], video_id)

        if _max_cursor != max_cursor:
            self.download_user_post(sec_uid, _signature, PAGE_NUM, _max_cursor)

    def download_user_like(self, sec_uid, _signature, _count=9, _max_cursor=0):
        """
         下载喜欢
        :param sec_uid:
        :param _signature:
        :param _count:
        :param _max_cursor:
        :return:
        """
        post_data = ''
        while True:
            content = requests.get(url=user_like, params={
                "sec_uid": str(sec_uid),
                "count": 100,
                "max_cursor": str(_max_cursor),
                "aid": 1128,
                "_signature": str(_signature),
                "dytk": "",
            }, allow_redirects=False).text.replace("\n", "")
            post_data = json.loads(content)
            if len(post_data['aweme_list']) > 0:
                break
            time.sleep(1)

        print("获取分页数据成功")
        max_cursor = post_data['max_cursor']
        print("最新_cursor", max_cursor)
        for x in post_data['aweme_list']:
            video_id = x['aweme_id']
            download(x['video']['play_addr']['url_list'][0], video_id)

        if _max_cursor != max_cursor:
            self.download_user_like(sec_uid, _signature, PAGE_NUM, _max_cursor)

    def download_challenge_videos(self, url, _count=9):
        """
        下载挑战视频
        :param url: 视频地址
        :param _count: 视频分页数量
        :return:
        """
        challenge_id = get_dy_url_id(url, "/?")

        challenge_info = requests.get(url=challenge_info_url, params={
            "ch_id": str(challenge_id)
        }).json()

        print(challenge_info)
        # 总数量
        user_count = challenge_info['ch_info']['user_count']
        cursor = 0
        if _count != 9:
            cursor = _count + PAGE_NUM
        data = requests.get(url=challenge_url, params={
            "ch_id": str(challenge_id),
            "count": _count,
            "cursor": cursor,
            "aid": 1128,
            "screen_limit": 3,
            "download_click_limit": 0,
            "_signature": generate_signature(str(challenge_id))
        }).json()
        for x in data['aweme_list']:
            download(x['video']['play_addr']['url_list'][0].replace('playwm', "play"), x['aweme_id'])

        if _count <= user_count:
            _count += PAGE_NUM
            self.download_challenge_videos(url=url, _count=_count)

    def download_music_videos(self, url, _count=9):
        """
        根据音乐下载
        :param url: 地址
        :param _count: 分页数量
        :return:
        """
        music_id = get_dy_url_id(url)
        # music_info = requests.get(url=music_info_url, params={
        #     "music_id": str(music_id)
        # }).json()
        cursor = 0
        if _count != 9:
            cursor = _count + PAGE_NUM
        data = requests.get(url=music_url, params={
            "music_id": str(music_id),
            "count": _count,
            "cursor": cursor,
            "aid": 1128,
            "screen_limit": 3,
            "download_click_limit": 0,
            "_signature": generate_signature(str(music_id))
        }).json()

        for x in data['aweme_list']:
            download(x['video']['play_addr']['url_list'][0].replace('playwm', "play"), x['aweme_id'])

        if data['has_more']:
            _count += PAGE_NUM
            self.download_music_videos(url=url, _count=_count)


if __name__ == '__main__':
    DouYinCrawler()
