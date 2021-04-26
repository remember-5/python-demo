import requests
import sys


if __name__ == '__main__':
    # base_url = "https://v.douyin.com/J6bwPep/"
    # base_url = "https://v.douyin.com/J6bwedp/"
    # base_url = "https://v.douyin.com/ekcnNt8/"
    base_url = sys.argv[1]
    play_id = requests.get(base_url, allow_redirects=False).headers['location'].split("/?")[0].split("/")[-1]
    data = requests.get("https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}&dytk=".format(play_id))
    real_url = data.json()['item_list'][0]['video']['play_addr']['url_list'][0].replace("playwm", "play")
    hd = {
        'authority': 'aweme.snssdk.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 '
    }
    url = requests.get(url=real_url, headers=hd, allow_redirects=False).headers['location']
    r = requests.get(url, stream=True)
    with open('{}.mp4'.format(play_id), "wb") as mp4:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp4.write(chunk)
    print("下载结束")
