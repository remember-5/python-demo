import tkinter
import re
import requests
import tkinter as tk
import tkinter.messagebox

from requests.exceptions import MissingSchema


def run(base_url):
    hd = {
        'authority': 'aweme.snssdk.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 '
    }
    # base_url = "https://v.douyin.com/J6bwPep/"
    # base_url = "https://v.douyin.com/J6bwedp/"
    # base_url = "https://v.douyin.com/ekcnNt8/"
    # base_url = "https://v.douyin.com/dYEAakK/"
    # base_url = sys.argv[1]
    try:
        play_id = requests.get(base_url, allow_redirects=False).headers['location'].split("/?")[0].split("/")[-1]
        # https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7002194140809186594&dytk=
        url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}&dytk=".format(play_id)
        data = requests.get(url, headers=hd)
        real_url = data.json()['item_list'][0]['video']['play_addr']['url_list'][0].replace("playwm", "play")
        url = requests.get(url=real_url, headers=hd, allow_redirects=False).headers['location']
        r = requests.get(url, stream=True)
        with open('{}.mp4'.format(play_id), "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)
        # print("下载结束")
        tkinter.messagebox.showinfo(title='提示', message='下载成功')
    except (BaseException, MissingSchema) as e:
        tkinter.messagebox.showwarning(title='提示', message='下载失败')


if __name__ == '__main__':
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    # run()
    window = tk.Tk()
    window.title('TikTok 无水印视频下载')
    # 窗口尺寸
    window.geometry('600x600')

    L1 = tk.Label(window, text="网站地址")
    L1.pack()

    e = tk.Entry(window, width="300")
    e.pack()


    def get_input_value():
        _url = e.get()
        if _url is None or "" == _url:
            tkinter.messagebox.showwarning(title='提示', message='不能输入空网址')
        else:
            run(pattern.findall(_url)[0])


    b = tk.Button(window, text="下载", width=15, height=2, command=get_input_value)
    b.pack()

    # 显示出来
    window.mainloop()
