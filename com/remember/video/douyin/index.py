import requests


def get_play_url(url):
    """
    获取无水印视频地址
    :param url: 分享的url
    :return: 视频地址
    """
    rep = requests.get(url=url, allow_redirects=False)
    # 获取视频的绝对地址
    video_url = rep.headers['location']

    url_path = video_url.split("/?")[0]
    video_id = url_path.split("/")[-1]

    data = requests.get(
        "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}&dytk=".format(video_id)).json()
    play_url = data['item_list'][0]['video']['play_addr']['url_list'][0].replace('playwm', "play")
    print(play_url)
    return play_url


def download(url):
    hd = {
        'authority': 'aweme.snssdk.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    rep = requests.get(url=url, headers=hd, allow_redirects=False)
    # 获取视频的绝对地址
    video_url = rep.headers['location']

    print("开始下载")
    r = requests.get(video_url, stream=True)

    with open('test.mp4', "wb") as mp4:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp4.write(chunk)

    print("下载结束")

    pass


if __name__ == '__main__':
    base_url = "https://v.douyin.com/J6CtsL7"
    play_url = get_play_url(base_url)
    download(play_url)
