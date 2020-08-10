import requests


class DouYinCrawler:

    def __init__(self, url=None):
        """
        init
        :param url: 需要爬取的url 如https://v.douyin.com/J6CtsL7
        """
        self.url = url
        self.get_play_url()

    def get_play_url(self):
        """
        获取无水印视频地址
        :return: 视频地址
        """
        # 先请求一次地址
        rep = requests.get(url=self.url, allow_redirects=False)

        # 在header中，能拿到视频有水印的视频地址
        watermark_url = rep.headers['location']
        print("watermark_url=", watermark_url)

        # 从url中取出视频的id
        video_id = watermark_url.split("/?")[0].split("/")[-1]
        self.video_id = video_id

        # IES(Information Exchange Service 信息交流处) 视频地址
        data = requests.get(
            "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}&dytk=".format(video_id)).json()
        play_url = data['item_list'][0]['video']['play_addr']['url_list'][0].replace('playwm', "play")
        print(play_url)
        self.download(play_url)

    def download(self, url):
        """
        下载视频
        :param url: 无水印播放地址
        :return:
        """
        hd = {
            'authority': 'aweme.snssdk.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 '
        }
        rep = requests.get(url=url, headers=hd, allow_redirects=False)
        # 获取视频的绝对地址
        video_url = rep.headers['location']

        print("开始下载")
        r = requests.get(video_url, stream=True)

        with open('{}.mp4'.format(self.video_id), "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)

        print("下载结束")


if __name__ == '__main__':
    base_url = "https://v.douyin.com/J6CtsL7"
    DouYinCrawler(base_url)
