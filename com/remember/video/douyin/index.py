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

# TODO 更改为request.params的方式调用
base_url = "https://www.iesdouyin.com/web/api/v2"
ies_url = base_url + "/aweme/iteminfo/?item_ids={}&dytk="
user_post = base_url + "/aweme/post/?sec_uid={}&count={}&max_cursor={}&aid={}&_signature={}"
user_like = base_url + "/aweme/like/?sec_uid={}&count={}&max_cursor={}&aid={}}&_signature={}&dytk={}"
user_info_url = base_url + "/user/info/?sec_uid={}"

challenge_url = base_url + "/challenge/aweme/"
challenge_info_url = base_url + "/challenge/info/"

music_url = base_url + "/music/list/aweme/"
music_info_url = base_url + "/music/info/"

hd = {
    'authority': 'aweme.snssdk.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                  'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

THREADS = 2

PAGE_NUM = 2

pool = ThreadPoolExecutor(10)
# HEADERS = {
#     'authority': 'aweme.snssdk.com',
#     'connection': 'keep-alive',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
#                   'Version/13.0.3 Mobile/15E148 Safari/604.1'
# }

HEADERS = {
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


def get_dy_url_id(url):
    return url.split("/?")[0].split("/")[-1]


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
    # print(target_folder)
    # print(os.path.exists(target_folder))
    if not os.path.exists(target_folder):
        # os.mkdir(target_folder)
        video_url = requests.get(url=url, headers=hd, allow_redirects=False).headers['location']
        print("video_url", video_url)

        # 获取视频的绝对地址
        print("开始下载")
        r = requests.get(video_url, stream=True)

        with open('../download/{}.mp4'.format(video_id), "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)

        print("下载结束")
    else:
        print("文件已经存在")


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

        for url in self.video:
            self.download_share_videos(url)
        for url in self.numbers:
            self.download_user_videos(url)
        for url in self.challenges:
            self.download_challenge_videos(url)
        for url in self.musics:
            self.download_music_videos(url)
        return

    def download_share_videos(self, url):
        """
        下载用户分享视频
        :param url: 视频地址
        """
        # 从url中取出视频的id
        video_id = get_dy_url_id(url)
        data = requests.get(ies_url.format(video_id)).json()
        play_url = data['item_list'][0]['video']['play_addr']['url_list'][0].replace('playwm', "play")
        download(play_url, video_id)

    def download_user_videos(self, url, _max_cursor=0):
        """
        下载用户的视频，包括作品和喜欢
        :param url:
        :param _max_cursor:
        :return:
        """
        print("当前url", url)
        print("当前_max_cursor", _max_cursor)
        # 获取sec_uid
        params = parse.parse_qs(parse.urlparse(url).query)
        sec_uid = params['sec_uid'][0]

        # 获取uid
        user_info = requests.get(user_info_url.format(sec_uid)).json()
        uid = user_info['user_info']['uid']  # 用户id
        _signature = generate_signature(uid)

        # 下载作品
        post_url = user_post.format(sec_uid, 100, _max_cursor, 1128, _signature, "")
        print(post_url)
        self.page_download(post_url, _max_cursor)

        # 下载喜欢
        like_url = user_like.format(sec_uid, 100, _max_cursor, 1128, _signature, "")
        print(like_url)
        self.page_download(like_url, _max_cursor)

    def page_download(self, url, _max_cursor):
        """
        分页下载
        :param url:
        :param _max_cursor:
        :return:
        """
        post_data = ''
        while True:
            post_data = json.loads(requests.get(url, allow_redirects=False).text.replace("\n", ""))
            # post_data = '{"status_code":0,"aweme_list":[{"statistics":{"play_count":0,"share_count":149,"forward_count":17,"aweme_id":"6858191037760883976","comment_count":1437,"digg_count":23000},"geofencing":null,"promotions":null,"desc":"欧洲杯上的旷古神话 P2","image_infos":null,"comment_list":null,"video_text":null,"aweme_id":"6858191037760883976","author":{"platform_sync_info":null,"has_orders":false,"policy_version":null,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","follow_status":0,"is_ad_fake":false,"with_commerce_entry":false,"enterprise_verify_reason":"","secret":0,"video_icon":{"uri":"","url_list":[]},"following_count":561,"total_favorited":"1731289","story_open":false,"with_shop_entry":false,"short_id":"2159699798","aweme_count":56,"geofencing":null,"user_canceled":false,"is_gov_media_vip":false,"avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"original_musician":{"music_count":0,"music_used_count":0},"verification_type":1,"region":"CN","avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"favoriting_count":2726,"with_fusion_shop_entry":false,"signature":"一个从98年爱上足球的伪球迷聊聊关于足球的故事⚽️微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","custom_verify":"","rate":1,"uid":"3927074991252420","nickname":"白日梦想家史瓦尼","followers_detail":null,"type_label":[],"follower_count":331330,"unique_id":"DayDreamSchwein"},"cha_list":null,"text_extra":[],"video_labels":null,"long_video":null,"video":{"origin_cover":{"url_list":["https://p3-dy-ipv6.byteimg.com/tos-cn-p-0015/397903d6a3274551821002f82a349f08_1596797054~tplv-dy-360p.jpeg?from=2563711402","https://p9-dy.byteimg.com/tos-cn-p-0015/397903d6a3274551821002f82a349f08_1596797054~tplv-dy-360p.jpeg?from=2563711402","https://p29-dy.byteimg.com/tos-cn-p-0015/397903d6a3274551821002f82a349f08_1596797054~tplv-dy-360p.jpeg?from=2563711402"],"uri":"tos-cn-p-0015/397903d6a3274551821002f82a349f08_1596797054"},"duration":292965,"play_addr":{"url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200fe00000bsmiv854688tg91u0gr0&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200fe00000bsmiv854688tg91u0gr0&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"],"uri":"v0200fe00000bsmiv854688tg91u0gr0"},"cover":{"uri":"tos-cn-p-0015/9561645a61cb4194a8c780592c628157","url_list":["https://p3-dy-ipv6.byteimg.com/img/tos-cn-p-0015/9561645a61cb4194a8c780592c628157~c5_300x400.jpeg?from=2563711402_large","https://p1-dy.byteimg.com/img/tos-cn-p-0015/9561645a61cb4194a8c780592c628157~c5_300x400.jpeg?from=2563711402_large","https://p9-dy.byteimg.com/img/tos-cn-p-0015/9561645a61cb4194a8c780592c628157~c5_300x400.jpeg?from=2563711402_large"]},"ratio":"540p","has_watermark":true,"is_long_video":1,"width":720,"dynamic_cover":{"uri":"tos-cn-p-0015/17f4812fe1754daf8bb544b8846e32f6_1596797055","url_list":["https://p9-dy.byteimg.com/obj/tos-cn-p-0015/17f4812fe1754daf8bb544b8846e32f6_1596797055?from=2563711402_large","https://p29-dy.byteimg.com/obj/tos-cn-p-0015/17f4812fe1754daf8bb544b8846e32f6_1596797055?from=2563711402_large","https://p3-dy.byteimg.com/obj/tos-cn-p-0015/17f4812fe1754daf8bb544b8846e32f6_1596797055?from=2563711402_large"]},"vid":"v0200fe00000bsmiv854688tg91u0gr0","download_addr":{"uri":"v0200fe00000bsmiv854688tg91u0gr0","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200fe00000bsmiv854688tg91u0gr0&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200fe00000bsmiv854688tg91u0gr0&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]},"play_addr_lowbr":{"uri":"v0200fe00000bsmiv854688tg91u0gr0","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200fe00000bsmiv854688tg91u0gr0&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200fe00000bsmiv854688tg91u0gr0&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"height":1280,"bit_rate":null},"aweme_type":4,"label_top_text":null},{"geofencing":null,"promotions":null,"aweme_id":"6855968272760835336","comment_list":null,"text_extra":[],"aweme_type":4,"desc":"欧洲杯上的旷古神话  P1","author":{"geofencing":null,"rate":1,"with_commerce_entry":false,"is_ad_fake":false,"video_icon":{"url_list":[],"uri":""},"user_canceled":false,"policy_version":null,"uid":"3927074991252420","short_id":"2159699798","avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"following_count":561,"story_open":false,"with_shop_entry":false,"secret":0,"signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"aweme_count":56,"unique_id":"DayDreamSchwein","verification_type":1,"is_gov_media_vip":false,"type_label":[],"nickname":"白日梦想家史瓦尼","follow_status":0,"follower_count":331330,"total_favorited":"1731289","followers_detail":null,"favoriting_count":2726,"enterprise_verify_reason":"","platform_sync_info":null,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"custom_verify":"","region":"CN","has_orders":false,"with_fusion_shop_entry":false,"original_musician":{"music_count":0,"music_used_count":0}},"statistics":{"aweme_id":"6855968272760835336","comment_count":1291,"digg_count":11000,"play_count":0,"share_count":63,"forward_count":6},"video_labels":null,"image_infos":null,"video_text":null,"label_top_text":null,"long_video":null,"cha_list":null,"video":{"width":720,"bit_rate":null,"cover":{"uri":"tos-cn-p-0015/6a5d66ee1e70497599babc815fe11f91","url_list":["https://p29-dy.byteimg.com/img/tos-cn-p-0015/6a5d66ee1e70497599babc815fe11f91~c5_300x400.jpeg?from=2563711402_large","https://p26-dy.byteimg.com/img/tos-cn-p-0015/6a5d66ee1e70497599babc815fe11f91~c5_300x400.jpeg?from=2563711402_large","https://p9-dy.byteimg.com/img/tos-cn-p-0015/6a5d66ee1e70497599babc815fe11f91~c5_300x400.jpeg?from=2563711402_large"]},"play_addr_lowbr":{"uri":"v0200f4f0000bsikjtgop6u9lhfrbbpg","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f4f0000bsikjtgop6u9lhfrbbpg&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f4f0000bsikjtgop6u9lhfrbbpg&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"duration":261502,"play_addr":{"url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f4f0000bsikjtgop6u9lhfrbbpg&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f4f0000bsikjtgop6u9lhfrbbpg&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"],"uri":"v0200f4f0000bsikjtgop6u9lhfrbbpg"},"dynamic_cover":{"uri":"tos-cn-p-0015/2e2d0952576f4600bcfbaadb5f7d72e7_1596279531","url_list":["https://p29-dy.byteimg.com/obj/tos-cn-p-0015/2e2d0952576f4600bcfbaadb5f7d72e7_1596279531?from=2563711402_large","https://p9-dy.byteimg.com/obj/tos-cn-p-0015/2e2d0952576f4600bcfbaadb5f7d72e7_1596279531?from=2563711402_large","https://p26-dy.byteimg.com/obj/tos-cn-p-0015/2e2d0952576f4600bcfbaadb5f7d72e7_1596279531?from=2563711402_large"]},"has_watermark":true,"vid":"v0200f4f0000bsikjtgop6u9lhfrbbpg","is_long_video":1,"height":1280,"origin_cover":{"uri":"tos-cn-p-0015/4b9826639a544b59aa844c0839df2411_1596279529","url_list":["https://p29-dy.byteimg.com/tos-cn-p-0015/4b9826639a544b59aa844c0839df2411_1596279529~tplv-dy-360p.jpeg?from=2563711402","https://p9-dy.byteimg.com/tos-cn-p-0015/4b9826639a544b59aa844c0839df2411_1596279529~tplv-dy-360p.jpeg?from=2563711402","https://p26-dy.byteimg.com/tos-cn-p-0015/4b9826639a544b59aa844c0839df2411_1596279529~tplv-dy-360p.jpeg?from=2563711402"]},"ratio":"540p","download_addr":{"uri":"v0200f4f0000bsikjtgop6u9lhfrbbpg","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f4f0000bsikjtgop6u9lhfrbbpg&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200f4f0000bsikjtgop6u9lhfrbbpg&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]}}},{"text_extra":[],"aweme_type":4,"label_top_text":null,"video":{"cover":{"uri":"tos-cn-p-0015/b1aeb9b926d947d392afa916beebe91c","url_list":["https://p26-dy.byteimg.com/img/tos-cn-p-0015/b1aeb9b926d947d392afa916beebe91c~c5_300x400.jpeg?from=2563711402_large","https://p9-dy.byteimg.com/img/tos-cn-p-0015/b1aeb9b926d947d392afa916beebe91c~c5_300x400.jpeg?from=2563711402_large","https://p3-dy.byteimg.com/img/tos-cn-p-0015/b1aeb9b926d947d392afa916beebe91c~c5_300x400.jpeg?from=2563711402_large"]},"height":1280,"download_addr":{"uri":"v0200f870000bsdc7m8h482t3h5epfng","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f870000bsdc7m8h482t3h5epfng&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200f870000bsdc7m8h482t3h5epfng&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]},"play_addr_lowbr":{"uri":"v0200f870000bsdc7m8h482t3h5epfng","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f870000bsdc7m8h482t3h5epfng&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f870000bsdc7m8h482t3h5epfng&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"width":720,"origin_cover":{"uri":"tos-cn-p-0015/a1686f55d927447d949ae664de03254a_1595589635","url_list":["https://p6-dy-ipv6.byteimg.com/tos-cn-p-0015/a1686f55d927447d949ae664de03254a_1595589635~tplv-dy-360p.jpeg?from=2563711402","https://p9-dy.byteimg.com/tos-cn-p-0015/a1686f55d927447d949ae664de03254a_1595589635~tplv-dy-360p.jpeg?from=2563711402","https://p26-dy.byteimg.com/tos-cn-p-0015/a1686f55d927447d949ae664de03254a_1595589635~tplv-dy-360p.jpeg?from=2563711402"]},"has_watermark":true,"ratio":"540p","duration":224095,"is_long_video":1,"play_addr":{"uri":"v0200f870000bsdc7m8h482t3h5epfng","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f870000bsdc7m8h482t3h5epfng&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f870000bsdc7m8h482t3h5epfng&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"dynamic_cover":{"uri":"tos-cn-p-0015/582bab4b1d3f47a087617b4180e772f4_1595589634","url_list":["https://p3-dy-ipv6.byteimg.com/obj/tos-cn-p-0015/582bab4b1d3f47a087617b4180e772f4_1595589634?from=2563711402_large","https://p9-dy.byteimg.com/obj/tos-cn-p-0015/582bab4b1d3f47a087617b4180e772f4_1595589634?from=2563711402_large","https://p29-dy.byteimg.com/obj/tos-cn-p-0015/582bab4b1d3f47a087617b4180e772f4_1595589634?from=2563711402_large"]},"bit_rate":null,"vid":"v0200f870000bsdc7m8h482t3h5epfng"},"video_labels":null,"image_infos":null,"long_video":null,"author":{"nickname":"白日梦想家史瓦尼","follow_status":0,"total_favorited":"1731289","rate":1,"aweme_count":56,"favoriting_count":2726,"verification_type":1,"policy_version":null,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","type_label":[],"signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","follower_count":331330,"custom_verify":"","followers_detail":null,"secret":0,"avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"is_ad_fake":false,"region":"CN","video_icon":{"uri":"","url_list":[]},"user_canceled":false,"avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"following_count":561,"enterprise_verify_reason":"","with_fusion_shop_entry":false,"short_id":"2159699798","with_commerce_entry":false,"original_musician":{"music_count":0,"music_used_count":0},"with_shop_entry":false,"is_gov_media_vip":false,"uid":"3927074991252420","unique_id":"DayDreamSchwein","story_open":false,"platform_sync_info":null,"has_orders":false,"geofencing":null},"cha_list":null,"video_text":null,"aweme_id":"6853005207983377672","desc":"曾经闪耀世青赛的超白金一代 P3","statistics":{"comment_count":361,"digg_count":4522,"play_count":0,"share_count":52,"forward_count":10,"aweme_id":"6853005207983377672"},"comment_list":null,"geofencing":null,"promotions":null},{"video":{"has_watermark":true,"origin_cover":{"uri":"tos-cn-p-0015/c317be73be674dfa808488280467b711_1595070915","url_list":["https://p9-dy.byteimg.com/tos-cn-p-0015/c317be73be674dfa808488280467b711_1595070915~tplv-dy-360p.jpeg?from=2563711402","https://p6-dy-ipv6.byteimg.com/tos-cn-p-0015/c317be73be674dfa808488280467b711_1595070915~tplv-dy-360p.jpeg?from=2563711402","https://p3-dy.byteimg.com/tos-cn-p-0015/c317be73be674dfa808488280467b711_1595070915~tplv-dy-360p.jpeg?from=2563711402"]},"width":720,"download_addr":{"url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f380000bs9dj1nrv8m7h96ir8sg&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200f380000bs9dj1nrv8m7h96ir8sg&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"],"uri":"v0200f380000bs9dj1nrv8m7h96ir8sg"},"play_addr":{"uri":"v0200f380000bs9dj1nrv8m7h96ir8sg","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f380000bs9dj1nrv8m7h96ir8sg&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f380000bs9dj1nrv8m7h96ir8sg&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"play_addr_lowbr":{"uri":"v0200f380000bs9dj1nrv8m7h96ir8sg","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f380000bs9dj1nrv8m7h96ir8sg&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f380000bs9dj1nrv8m7h96ir8sg&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"duration":197787,"vid":"v0200f380000bs9dj1nrv8m7h96ir8sg","ratio":"540p","height":1280,"dynamic_cover":{"uri":"tos-cn-p-0015/a2bac2ac6f984e42a37cb8d425ed2c9f_1595070916","url_list":["https://p29-dy.byteimg.com/obj/tos-cn-p-0015/a2bac2ac6f984e42a37cb8d425ed2c9f_1595070916?from=2563711402_large","https://p3-dy.byteimg.com/obj/tos-cn-p-0015/a2bac2ac6f984e42a37cb8d425ed2c9f_1595070916?from=2563711402_large","https://p6-dy-ipv6.byteimg.com/obj/tos-cn-p-0015/a2bac2ac6f984e42a37cb8d425ed2c9f_1595070916?from=2563711402_large"]},"bit_rate":null,"is_long_video":1,"cover":{"uri":"tos-cn-p-0015/5ee8da8a1c9e404fb1497b7ed6ff137d","url_list":["https://p9-dy.byteimg.com/img/tos-cn-p-0015/5ee8da8a1c9e404fb1497b7ed6ff137d~c5_300x400.jpeg?from=2563711402_large","https://p3-dy.byteimg.com/img/tos-cn-p-0015/5ee8da8a1c9e404fb1497b7ed6ff137d~c5_300x400.jpeg?from=2563711402_large","https://p29-dy.byteimg.com/img/tos-cn-p-0015/5ee8da8a1c9e404fb1497b7ed6ff137d~c5_300x400.jpeg?from=2563711402_large"]}},"author":{"rate":1,"type_label":[],"nickname":"白日梦想家史瓦尼","aweme_count":56,"is_ad_fake":false,"followers_detail":null,"geofencing":null,"with_fusion_shop_entry":false,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","following_count":561,"total_favorited":"1731289","region":"CN","secret":0,"with_commerce_entry":false,"has_orders":false,"is_gov_media_vip":false,"short_id":"2159699798","avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"follow_status":0,"unique_id":"DayDreamSchwein","follower_count":331330,"original_musician":{"music_count":0,"music_used_count":0},"uid":"3927074991252420","signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","with_shop_entry":false,"avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"favoriting_count":2726,"verification_type":1,"video_icon":{"uri":"","url_list":[]},"custom_verify":"","enterprise_verify_reason":"","platform_sync_info":null,"policy_version":null,"avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"story_open":false,"user_canceled":false},"cha_list":null,"statistics":{"forward_count":2,"aweme_id":"6850777150857956615","comment_count":456,"digg_count":4236,"play_count":0,"share_count":53},"label_top_text":null,"video_text":null,"promotions":null,"text_extra":[{"start":19,"end":24,"type":1,"hashtag_name":"遇见足球","hashtag_id":1665493680955469}],"image_infos":null,"comment_list":null,"geofencing":null,"long_video":null,"aweme_id":"6850777150857956615","desc":"曾经闪耀世青赛的81超白金一代 P2 #遇见足球","video_labels":null,"aweme_type":4},{"desc":"曾闪耀世青赛的81“超白金一代” P1 #遇见足球","comment_list":null,"video_text":null,"label_top_text":null,"text_extra":[{"type":1,"hashtag_name":"遇见足球","hashtag_id":1665493680955469,"start":20,"end":25}],"aweme_type":4,"image_infos":null,"promotions":null,"aweme_id":"6848931609157143821","cha_list":null,"video_labels":null,"geofencing":null,"long_video":null,"author":{"following_count":561,"is_ad_fake":false,"followers_detail":null,"platform_sync_info":null,"with_shop_entry":false,"secret":0,"geofencing":null,"avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"policy_version":null,"with_fusion_shop_entry":false,"verification_type":1,"has_orders":false,"is_gov_media_vip":false,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","type_label":[],"avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"total_favorited":"1731289","unique_id":"DayDreamSchwein","signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","with_commerce_entry":false,"enterprise_verify_reason":"","user_canceled":false,"avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"original_musician":{"music_count":0,"music_used_count":0},"video_icon":{"uri":"","url_list":[]},"story_open":false,"nickname":"白日梦想家史瓦尼","aweme_count":56,"follower_count":331330,"favoriting_count":2726,"rate":1,"short_id":"2159699798","follow_status":0,"region":"CN","uid":"3927074991252420","custom_verify":""},"video":{"origin_cover":{"uri":"tos-cn-p-0015/2e6dac85deb64a4c8eb765f657b6ee3b_1594641170","url_list":["https://p3-dy-ipv6.byteimg.com/tos-cn-p-0015/2e6dac85deb64a4c8eb765f657b6ee3b_1594641170~tplv-dy-360p.jpeg?from=2563711402","https://p1-dy.byteimg.com/tos-cn-p-0015/2e6dac85deb64a4c8eb765f657b6ee3b_1594641170~tplv-dy-360p.jpeg?from=2563711402","https://p9-dy.byteimg.com/tos-cn-p-0015/2e6dac85deb64a4c8eb765f657b6ee3b_1594641170~tplv-dy-360p.jpeg?from=2563711402"]},"play_addr_lowbr":{"uri":"v0200f0e0000bs64lmfh3dfiv1hhqj1g","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f0e0000bs64lmfh3dfiv1hhqj1g&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f0e0000bs64lmfh3dfiv1hhqj1g&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"duration":143659,"cover":{"uri":"tos-cn-p-0015/fd97c43e204c467aaf5ad31223135ad2","url_list":["https://p29-dy.byteimg.com/img/tos-cn-p-0015/fd97c43e204c467aaf5ad31223135ad2~c5_300x400.jpeg?from=2563711402_large","https://p9-dy.byteimg.com/img/tos-cn-p-0015/fd97c43e204c467aaf5ad31223135ad2~c5_300x400.jpeg?from=2563711402_large","https://p26-dy.byteimg.com/img/tos-cn-p-0015/fd97c43e204c467aaf5ad31223135ad2~c5_300x400.jpeg?from=2563711402_large"]},"height":1280,"width":720,"dynamic_cover":{"uri":"tos-cn-p-0015/1f3012ebb2ea420c83d90272b3565541_1594641173","url_list":["https://p9-dy.byteimg.com/obj/tos-cn-p-0015/1f3012ebb2ea420c83d90272b3565541_1594641173?from=2563711402_large","https://p6-dy-ipv6.byteimg.com/obj/tos-cn-p-0015/1f3012ebb2ea420c83d90272b3565541_1594641173?from=2563711402_large","https://p3-dy.byteimg.com/obj/tos-cn-p-0015/1f3012ebb2ea420c83d90272b3565541_1594641173?from=2563711402_large"]},"is_long_video":1,"ratio":"540p","download_addr":{"uri":"v0200f0e0000bs64lmfh3dfiv1hhqj1g","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f0e0000bs64lmfh3dfiv1hhqj1g&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200f0e0000bs64lmfh3dfiv1hhqj1g&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]},"vid":"v0200f0e0000bs64lmfh3dfiv1hhqj1g","play_addr":{"uri":"v0200f0e0000bs64lmfh3dfiv1hhqj1g","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f0e0000bs64lmfh3dfiv1hhqj1g&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f0e0000bs64lmfh3dfiv1hhqj1g&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"has_watermark":true,"bit_rate":null},"statistics":{"aweme_id":"6848931609157143821","comment_count":1167,"digg_count":14000,"play_count":0,"share_count":188,"forward_count":10}},{"video":{"download_addr":{"uri":"v0200f5a0000bs2qs3286o34jpsbsttg","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f5a0000bs2qs3286o34jpsbsttg&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200f5a0000bs2qs3286o34jpsbsttg&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]},"height":1280,"width":720,"dynamic_cover":{"uri":"tos-cn-p-0015/c3c12d3b4c3d47318cd94151e73002b5_1594207932","url_list":["https://p26-dy.byteimg.com/obj/tos-cn-p-0015/c3c12d3b4c3d47318cd94151e73002b5_1594207932?from=2563711402_large","https://p3-dy.byteimg.com/obj/tos-cn-p-0015/c3c12d3b4c3d47318cd94151e73002b5_1594207932?from=2563711402_large","https://p9-dy.byteimg.com/obj/tos-cn-p-0015/c3c12d3b4c3d47318cd94151e73002b5_1594207932?from=2563711402_large"]},"has_watermark":true,"bit_rate":null,"duration":231467,"is_long_video":1,"cover":{"uri":"tos-cn-p-0015/c3c0318a972445a4951a52f8e3eea034","url_list":["https://p3-dy-ipv6.byteimg.com/img/tos-cn-p-0015/c3c0318a972445a4951a52f8e3eea034~c5_300x400.jpeg?from=2563711402_large","https://p9-dy.byteimg.com/img/tos-cn-p-0015/c3c0318a972445a4951a52f8e3eea034~c5_300x400.jpeg?from=2563711402_large","https://p26-dy.byteimg.com/img/tos-cn-p-0015/c3c0318a972445a4951a52f8e3eea034~c5_300x400.jpeg?from=2563711402_large"]},"origin_cover":{"uri":"tos-cn-p-0015/6eb6cd8aeafc4ccd987c7a5408cb562c_1594207931","url_list":["https://p9-dy.byteimg.com/tos-cn-p-0015/6eb6cd8aeafc4ccd987c7a5408cb562c_1594207931~tplv-dy-360p.jpeg?from=2563711402","https://p3-dy.byteimg.com/tos-cn-p-0015/6eb6cd8aeafc4ccd987c7a5408cb562c_1594207931~tplv-dy-360p.jpeg?from=2563711402","https://p26-dy.byteimg.com/tos-cn-p-0015/6eb6cd8aeafc4ccd987c7a5408cb562c_1594207931~tplv-dy-360p.jpeg?from=2563711402"]},"ratio":"540p","play_addr_lowbr":{"uri":"v0200f5a0000bs2qs3286o34jpsbsttg","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f5a0000bs2qs3286o34jpsbsttg&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f5a0000bs2qs3286o34jpsbsttg&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"play_addr":{"uri":"v0200f5a0000bs2qs3286o34jpsbsttg","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f5a0000bs2qs3286o34jpsbsttg&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f5a0000bs2qs3286o34jpsbsttg&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"vid":"v0200f5a0000bs2qs3286o34jpsbsttg"},"aweme_type":4,"image_infos":null,"geofencing":null,"desc":"从全民公敌到国家英雄的自我救赎 P3 你们期待的时刻来了","author":{"uid":"3927074991252420","short_id":"2159699798","signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","following_count":561,"follower_count":331330,"geofencing":null,"avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"story_open":false,"secret":0,"has_orders":false,"follow_status":0,"custom_verify":"","enterprise_verify_reason":"","aweme_count":56,"verification_type":1,"original_musician":{"music_count":0,"music_used_count":0},"with_fusion_shop_entry":false,"user_canceled":false,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","unique_id":"DayDreamSchwein","with_shop_entry":false,"rate":1,"type_label":[],"with_commerce_entry":false,"is_ad_fake":false,"video_icon":{"uri":"","url_list":[]},"platform_sync_info":null,"nickname":"白日梦想家史瓦尼","avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"avatar_medium":{"url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"],"uri":"3120e000444af19a5f6b8"},"total_favorited":"1731289","followers_detail":null,"region":"CN","favoriting_count":2726,"is_gov_media_vip":false,"policy_version":null},"promotions":null,"cha_list":null,"statistics":{"comment_count":1046,"digg_count":18000,"play_count":0,"share_count":98,"forward_count":22,"aweme_id":"6847070829264637197"},"text_extra":[],"video_labels":null,"comment_list":null,"video_text":null,"aweme_id":"6847070829264637197","label_top_text":null,"long_video":null},{"desc":"从全民公敌到国家英雄的自我救赎 P2","author":{"follow_status":0,"custom_verify":"","region":"CN","with_fusion_shop_entry":false,"is_ad_fake":false,"rate":1,"uid":"3927074991252420","avatar_larger":{"url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"],"uri":"3120e000444af19a5f6b8"},"avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"geofencing":null,"policy_version":null,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","short_id":"2159699798","follower_count":331330,"platform_sync_info":null,"with_shop_entry":false,"video_icon":{"uri":"","url_list":[]},"user_canceled":false,"avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"unique_id":"DayDreamSchwein","followers_detail":null,"secret":0,"story_open":false,"with_commerce_entry":false,"enterprise_verify_reason":"","has_orders":false,"total_favorited":"1731289","original_musician":{"music_used_count":0,"music_count":0},"is_gov_media_vip":false,"nickname":"白日梦想家史瓦尼","signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","aweme_count":56,"favoriting_count":2726,"following_count":561,"verification_type":1,"type_label":[]},"text_extra":[],"aweme_type":4,"promotions":null,"video_labels":null,"aweme_id":"6845095445295844622","video":{"ratio":"540p","bit_rate":null,"height":1280,"dynamic_cover":{"uri":"tos-cn-p-0015/6a9301bb9986417caca42b3fffa48688_1593748002","url_list":["https://p3-dy-ipv6.byteimg.com/obj/tos-cn-p-0015/6a9301bb9986417caca42b3fffa48688_1593748002?from=2563711402_large","https://p9-dy.byteimg.com/obj/tos-cn-p-0015/6a9301bb9986417caca42b3fffa48688_1593748002?from=2563711402_large","https://p29-dy.byteimg.com/obj/tos-cn-p-0015/6a9301bb9986417caca42b3fffa48688_1593748002?from=2563711402_large"]},"download_addr":{"uri":"v0200fd10000brvajf49hq5pfpblfg3g","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200fd10000brvajf49hq5pfpblfg3g&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200fd10000brvajf49hq5pfpblfg3g&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]},"duration":152624,"play_addr":{"uri":"v0200fd10000brvajf49hq5pfpblfg3g","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200fd10000brvajf49hq5pfpblfg3g&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200fd10000brvajf49hq5pfpblfg3g&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"cover":{"uri":"tos-cn-p-0015/e760247187f043cdab0c26efd110e9fd","url_list":["https://p3-dy-ipv6.byteimg.com/img/tos-cn-p-0015/e760247187f043cdab0c26efd110e9fd~c5_300x400.jpeg?from=2563711402_large","https://p9-dy.byteimg.com/img/tos-cn-p-0015/e760247187f043cdab0c26efd110e9fd~c5_300x400.jpeg?from=2563711402_large","https://p26-dy.byteimg.com/img/tos-cn-p-0015/e760247187f043cdab0c26efd110e9fd~c5_300x400.jpeg?from=2563711402_large"]},"has_watermark":true,"width":720,"origin_cover":{"uri":"tos-cn-p-0015/8664e17ba7ee4ee3893dbe68b34694d6_1593748002","url_list":["https://p6-dy-ipv6.byteimg.com/tos-cn-p-0015/8664e17ba7ee4ee3893dbe68b34694d6_1593748002~tplv-dy-360p.jpeg?from=2563711402","https://p9-dy.byteimg.com/tos-cn-p-0015/8664e17ba7ee4ee3893dbe68b34694d6_1593748002~tplv-dy-360p.jpeg?from=2563711402","https://p29-dy.byteimg.com/tos-cn-p-0015/8664e17ba7ee4ee3893dbe68b34694d6_1593748002~tplv-dy-360p.jpeg?from=2563711402"]},"play_addr_lowbr":{"uri":"v0200fd10000brvajf49hq5pfpblfg3g","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200fd10000brvajf49hq5pfpblfg3g&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200fd10000brvajf49hq5pfpblfg3g&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"vid":"v0200fd10000brvajf49hq5pfpblfg3g","is_long_video":1},"statistics":{"forward_count":12,"aweme_id":"6845095445295844622","comment_count":485,"digg_count":15000,"play_count":0,"share_count":56},"comment_list":null,"geofencing":null,"cha_list":null,"image_infos":null,"video_text":null,"label_top_text":null,"long_video":null},{"cha_list":null,"video_labels":null,"aweme_type":4,"image_infos":null,"aweme_id":"6843723913566915853","author":{"geofencing":null,"is_gov_media_vip":false,"avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"has_orders":false,"uid":"3927074991252420","following_count":561,"original_musician":{"music_used_count":0,"music_count":0},"region":"CN","type_label":[],"follower_count":331330,"with_commerce_entry":false,"enterprise_verify_reason":"","with_fusion_shop_entry":false,"policy_version":null,"nickname":"白日梦想家史瓦尼","total_favorited":"1731289","rate":1,"follow_status":0,"unique_id":"DayDreamSchwein","story_open":false,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","user_canceled":false,"short_id":"2159699798","avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"avatar_thumb":{"uri":"3120e000444af19a5f6b8","url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"is_ad_fake":false,"followers_detail":null,"platform_sync_info":null,"with_shop_entry":false,"secret":0,"signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","aweme_count":56,"favoriting_count":2726,"custom_verify":"","verification_type":1,"video_icon":{"uri":"","url_list":[]}},"comment_list":null,"label_top_text":null,"promotions":null,"desc":"从全民公敌到国家英雄的自我救赎  P1","statistics":{"aweme_id":"6843723913566915853","comment_count":1197,"digg_count":44000,"play_count":0,"share_count":198,"forward_count":21},"text_extra":[],"video_text":null,"video":{"duration":165418,"ratio":"540p","download_addr":{"uri":"v0200f4f0000brssku52v32d84cjcdp0","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f4f0000brssku52v32d84cjcdp0&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200f4f0000brssku52v32d84cjcdp0&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]},"has_watermark":true,"vid":"v0200f4f0000brssku52v32d84cjcdp0","play_addr_lowbr":{"uri":"v0200f4f0000brssku52v32d84cjcdp0","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f4f0000brssku52v32d84cjcdp0&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f4f0000brssku52v32d84cjcdp0&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"is_long_video":1,"play_addr":{"uri":"v0200f4f0000brssku52v32d84cjcdp0","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f4f0000brssku52v32d84cjcdp0&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f4f0000brssku52v32d84cjcdp0&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"cover":{"uri":"tos-cn-p-0015/13da75f6347b485d89118d1054b3c3de","url_list":["https://p3-dy-ipv6.byteimg.com/img/tos-cn-p-0015/13da75f6347b485d89118d1054b3c3de~c5_300x400.jpeg?from=2563711402_large","https://p1-dy.byteimg.com/img/tos-cn-p-0015/13da75f6347b485d89118d1054b3c3de~c5_300x400.jpeg?from=2563711402_large","https://p6-dy-ipv6.byteimg.com/img/tos-cn-p-0015/13da75f6347b485d89118d1054b3c3de~c5_300x400.jpeg?from=2563711402_large"]},"width":720,"origin_cover":{"uri":"tos-cn-p-0015/3b23fa3cb6b74cd1bdb8c88dca0c4a80_1593428660","url_list":["https://p29-dy.byteimg.com/tos-cn-p-0015/3b23fa3cb6b74cd1bdb8c88dca0c4a80_1593428660~tplv-dy-360p.jpeg?from=2563711402","https://p1-dy.byteimg.com/tos-cn-p-0015/3b23fa3cb6b74cd1bdb8c88dca0c4a80_1593428660~tplv-dy-360p.jpeg?from=2563711402","https://p9-dy.byteimg.com/tos-cn-p-0015/3b23fa3cb6b74cd1bdb8c88dca0c4a80_1593428660~tplv-dy-360p.jpeg?from=2563711402"]},"height":1280,"dynamic_cover":{"uri":"tos-cn-p-0015/0edae726b4114ab2b30630f119014473_1593428661","url_list":["https://p29-dy.byteimg.com/obj/tos-cn-p-0015/0edae726b4114ab2b30630f119014473_1593428661?from=2563711402_large","https://p9-dy.byteimg.com/obj/tos-cn-p-0015/0edae726b4114ab2b30630f119014473_1593428661?from=2563711402_large","https://p3-dy.byteimg.com/obj/tos-cn-p-0015/0edae726b4114ab2b30630f119014473_1593428661?from=2563711402_large"]},"bit_rate":null},"long_video":null,"geofencing":null},{"aweme_id":"6841859672853597448","cha_list":null,"statistics":{"share_count":57,"forward_count":12,"aweme_id":"6841859672853597448","comment_count":879,"digg_count":5621,"play_count":0},"image_infos":null,"promotions":null,"long_video":null,"author":{"verification_type":1,"enterprise_verify_reason":"","followers_detail":null,"with_shop_entry":false,"avatar_medium":{"uri":"3120e000444af19a5f6b8","url_list":["https://p1-dy-ipv6.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p29-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/720x720/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"follower_count":331330,"story_open":false,"unique_id":"DayDreamSchwein","is_ad_fake":false,"secret":0,"nickname":"白日梦想家史瓦尼","avatar_larger":{"uri":"3120e000444af19a5f6b8","url_list":["https://p29-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p3-dy.byteimg.com/aweme/1080x1080/3120e000444af19a5f6b8.jpeg?from=4010531038"]},"custom_verify":"","original_musician":{"music_used_count":0,"music_count":0},"geofencing":null,"with_fusion_shop_entry":false,"sec_uid":"MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu","rate":1,"short_id":"2159699798","signature":"一个从98年爱上足球的伪球迷\n聊聊关于足球的故事\n⚽️\n微博&B站：白日梦想家史瓦尼\n⚽\n白天搬砖 晚上做片\n催更的小伙伴请谅解🙏🏻🙏🏻🙏🏻","avatar_thumb":{"url_list":["https://p3-dy-ipv6.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p26-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038","https://p9-dy.byteimg.com/aweme/100x100/3120e000444af19a5f6b8.jpeg?from=4010531038"],"uri":"3120e000444af19a5f6b8"},"following_count":561,"with_commerce_entry":false,"uid":"3927074991252420","follow_status":0,"aweme_count":56,"type_label":[],"platform_sync_info":null,"video_icon":{"uri":"","url_list":[]},"is_gov_media_vip":false,"policy_version":null,"favoriting_count":2726,"has_orders":false,"user_canceled":false,"region":"CN","total_favorited":"1731289"},"video":{"play_addr":{"uri":"v0200f090000brpiksspg62e27ho8jt0","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f090000brpiksspg62e27ho8jt0&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f090000brpiksspg62e27ho8jt0&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"height":1280,"has_watermark":true,"width":720,"play_addr_lowbr":{"uri":"v0200f090000brpiksspg62e27ho8jt0","url_list":["https://aweme-hl.snssdk.com/aweme/v1/play/?video_id=v0200f090000brpiksspg62e27ho8jt0&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH","https://api-hl.amemv.com/aweme/v1/play/?video_id=v0200f090000brpiksspg62e27ho8jt0&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&source=PackSourceEnum_PUBLISH"]},"bit_rate":null,"vid":"v0200f090000brpiksspg62e27ho8jt0","is_long_video":1,"cover":{"uri":"tos-cn-p-0015/8047c7e57dde486c98ca70fd2eef59f1","url_list":["https://p6-dy-ipv6.byteimg.com/img/tos-cn-p-0015/8047c7e57dde486c98ca70fd2eef59f1~c5_300x400.jpeg?from=2563711402_large","https://p1-dy.byteimg.com/img/tos-cn-p-0015/8047c7e57dde486c98ca70fd2eef59f1~c5_300x400.jpeg?from=2563711402_large","https://p29-dy.byteimg.com/img/tos-cn-p-0015/8047c7e57dde486c98ca70fd2eef59f1~c5_300x400.jpeg?from=2563711402_large"]},"dynamic_cover":{"uri":"tos-cn-p-0015/94991386878d4765884cc852201d40b5_1592994615","url_list":["https://p3-dy-ipv6.byteimg.com/obj/tos-cn-p-0015/94991386878d4765884cc852201d40b5_1592994615?from=2563711402_large","https://p9-dy.byteimg.com/obj/tos-cn-p-0015/94991386878d4765884cc852201d40b5_1592994615?from=2563711402_large","https://p29-dy.byteimg.com/obj/tos-cn-p-0015/94991386878d4765884cc852201d40b5_1592994615?from=2563711402_large"]},"origin_cover":{"uri":"tos-cn-p-0015/bd540064313846a1a015bc34695dba96_1592994616","url_list":["https://p3-dy-ipv6.byteimg.com/tos-cn-p-0015/bd540064313846a1a015bc34695dba96_1592994616~tplv-dy-360p.jpeg?from=2563711402","https://p9-dy.byteimg.com/tos-cn-p-0015/bd540064313846a1a015bc34695dba96_1592994616~tplv-dy-360p.jpeg?from=2563711402","https://p6-dy-ipv6.byteimg.com/tos-cn-p-0015/bd540064313846a1a015bc34695dba96_1592994616~tplv-dy-360p.jpeg?from=2563711402"]},"duration":165813,"ratio":"540p","download_addr":{"uri":"v0200f090000brpiksspg62e27ho8jt0","url_list":["https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f090000brpiksspg62e27ho8jt0&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH","https://api.amemv.com/aweme/v1/play/?video_id=v0200f090000brpiksspg62e27ho8jt0&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&source=PackSourceEnum_PUBLISH"]}},"video_text":null,"label_top_text":null,"desc":"欧锦赛名场面--刺激无比的金球加冕 P2","text_extra":[],"video_labels":null,"aweme_type":4,"comment_list":null,"geofencing":null}],"max_cursor":1592994613000,"min_cursor":1596797053000,"has_more":true,"extra":{"now":1597119524000,"logid":"202008111218440101960242033302F863"}}'
            # post_data = json.loads(post_data.replace("\n", ""))
            if len(post_data['aweme_list']) > 0:
                break
            time.sleep(1)

        print("获取分页成功")
        max_cursor = post_data['max_cursor']
        print("最新_cursor", max_cursor)
        for x in post_data['aweme_list']:
            video_id = x['aweme_id']
            download(x['video']['play_addr']['url_list'][0], video_id)

        if _max_cursor != max_cursor:
            self.download_user_videos(url=url, _max_cursor=max_cursor)

    def download_challenge_videos(self, url, _count=9):
        """
        下载挑战视频
        :param url: 视频地址
        :param _count: 视频分页数量
        :return:
        """
        challenge_id = get_dy_url_id(url)

        challenge_info = requests.get(url=challenge_info_url, params={
            "ch_id": str(challenge_id)
        }).json()

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
            video_id = x['aweme_id']
            download(x['video']['play_addr']['url_list'][0], video_id)

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
        music_id = url.split("?")[0].split("/")[-1]
        music_info = requests.get(url=music_info_url, params={
            "music_id": str(music_id)
        }).json()
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
            video_id = x['aweme_id']
            download(x['video']['play_addr']['url_list'][0], video_id)

        if data['has_more']:
            _count += PAGE_NUM
            self.download_music_videos(url=url, _count=_count)


if __name__ == '__main__':
    DouYinCrawler()
