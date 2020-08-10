import requests


def run(url):
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


if __name__ == '__main__':
    base_url = "https://v.douyin.com/J6CtsL7"
    run(base_url)
