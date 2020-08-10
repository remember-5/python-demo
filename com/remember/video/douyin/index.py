import requests
from urllib import parse

base_url = "https://www.iesdouyin.com/web/api/v2"
ies_url = base_url + "/aweme/iteminfo/?item_ids={}&dytk="
user_post = base_url + "/aweme/post/?sec_uid={}&count={}&max_cursor={}&aid={}&_signature={}"
user_like = base_url + "/aweme/like/?sec_uid={}&count={}&max_cursor={}&aid={}}&_signature={}&dytk={}"
get_user_info_url = base_url + "/user/info/?sec_uid={}"
hd = {
    'authority': 'aweme.snssdk.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                  'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 '
}


class DouYinCrawler:
    def __init__(self, url=None, user=None):
        """
        init
        :param url: 需要爬取的url
        """
        if url is None and user is None:
            print("地址和用户均为空，无法爬取！！！")
            return
        if user is None:
            self.url = url
            self.video_id = None
            self.get_play_url()
        else:
            self.user = user
            self.get_video_by_user()

    def get_play_url(self):
        """
        获取无水印视频地址
        :return: 视频地址
        """
        # 先请求一次地址,在header中，能拿到视频有水印的视频地址
        watermark_url = requests.get(url=self.url, allow_redirects=False).headers['location']
        print("watermark_url=", watermark_url)

        # 从url中取出视频的id
        video_id = watermark_url.split("/?")[0].split("/")[-1]
        self.video_id = video_id

        # IES(Information Exchange Service 信息交流处) 视频地址
        data = requests.get(ies_url.format(video_id)).json()
        play_url = data['item_list'][0]['video']['play_addr']['url_list'][0].replace('playwm', "play")
        print(play_url)
        self.download(play_url)

    def download(self, url):
        """
        下载视频
        :param url: 无水印播放地址
        :return:
        """
        # 获取视频的绝对地址
        video_url = requests.get(url=url, headers=hd, allow_redirects=False).headers['location']

        print("开始下载")
        r = requests.get(video_url, stream=True)

        with open('{}.mp4'.format(self.video_id), "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)

        print("下载结束")

    def get_video_by_user(self):
        """
        根据用户爬视频
        :return:
        """
        user_url = requests.get(url=self.user, headers=hd, allow_redirects=False).headers['location']
        # params = parse.parse_qs(parse.urlparse(user_url).query)
        # sec_uid = params['sec_uid'][0]
        # # sec_uid=MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu&count=100&max_cursor=0&aid=1128&_signature=yhCqeQAAlSoSNMELX8MxC8oQqm&dytk=
        # user_post.format(sec_uid, 100, 0, 1128, )
        return


if __name__ == '__main__':

    # 批量下载视频
    # for line in open('url.txt', 'r').readlines():
    #     line = line.strip('\n')  # 去掉换行符
    #     print(line)
    #     DouYinCrawler(url=line)

    # 根据用户下载视频
    for line in open('user.txt', 'r').readlines():
        line = line.strip('\n')  # 去掉换行符
        print(line)
        DouYinCrawler(user=line)
