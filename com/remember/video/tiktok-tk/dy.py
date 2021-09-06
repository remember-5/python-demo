import tkinter
import re
import requests
import tkinter as tk
import tkinter.messagebox

from requests.exceptions import MissingSchema


# base_url = "https://v.douyin.com/J6bwPep/"
# base_url = "https://v.douyin.com/J6bwedp/"
# base_url = "https://v.douyin.com/ekcnNt8/"
# base_url = "https://v.douyin.com/dYEAakK/"


def download(url, play_id):
    try:
        r = requests.get(url, stream=True)
        with open('{}.mp4'.format(play_id), "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)
        tkinter.messagebox.showinfo(title='提示', message='下载成功')
    except (BaseException, MissingSchema) as e:
        tkinter.messagebox.showwarning(title='提示', message='下载失败')


def get_real_download_url(base_url):
    hd = {
        'authority': 'aweme.snssdk.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 l ike Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 '
    }
    play_id = requests.get(base_url, allow_redirects=False).headers['location'].split("/?")[0].split("/")[-1]
    # https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7002194140809186594&dytk=
    url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}&dytk=".format(play_id)
    data = requests.get(url, headers=hd)
    real_url = data.json()['item_list'][0]['video']['play_addr']['url_list'][0].replace("playwm", "play")
    url = requests.get(url=real_url, headers=hd, allow_redirects=False).headers['location']
    return url, play_id


pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

copy_url = ""

window = tk.Tk()
window.title('TikTok 无水印视频下载')

# 窗口尺寸
window.geometry('600x600')

# url input lable
l1 = tk.Label(window, text="请输入分享链接")
l1.pack()

# url input
e1 = tk.Entry(window, width="300")
e1.pack()

# url input lable
l2 = tk.Label(window, text="真实下载链接")
l2.pack()

t = tk.Text(window, height=10)
t.pack()


def get_input_value():
    url, play_id = get_real_url()
    download(url, play_id)


def clipboard_append():
    window.clipboard_clear()
    window.clipboard_append(copy_url)
    window.update()


def get_real_url():
    input_url = e1.get()
    if input_url is None or "" == input_url:
        tkinter.messagebox.showwarning(title='提示', message='不能输入空网址')
    else:
        url, play_id = get_real_download_url(pattern.findall(input_url)[0])
        global copy_url
        copy_url = url
        t.delete('0.0', 'end')
        t.insert("insert", copy_url)
        return url, play_id


# download button
b1 = tk.Button(window, text="下载", width=15, height=2, command=get_input_value)
b1.pack()

b2 = tk.Button(window, text="获取真实下载链接", width=15, height=2, command=get_real_url)
b2.pack()

b3 = tk.Button(window, text="复制下载链接", width=15, height=2, command=clipboard_append)
b3.pack()

text1 = '''
在分享处输入抖音的链接，比如
8.46 caA:/ 风来了，照顾好自己，以后没有晚安和早安了。%海绵宝宝 %派大星   https://v.douyin.com/d66d8mY/ 
复製此lian接，打开Dou音搜索，値接观看视频！
或者
https://v.douyin.com/d66d8mY/

然后点击'下载' 即可下载到本目录中
点击'获取真实下载链接'即可获取无水印视频到真实链接
点击'复制下载链接'即可复制到粘贴板
'''

l3 = tk.Label(
    window,
    text=text1,  # 设置文本内容
    width=300,  # 设置label的宽度：30
    height=10,  # 设置label的高度：10
    justify='left',  # 设置文本对齐方式：左对齐
    anchor='nw',  # 设置文本在label的方位：西北方位
    font=('微软雅黑', 12),  # 设置字体：微软雅黑，字号：18
    fg='white',  # 设置前景色：白色
    bg='grey',  # 设置背景色：灰色
    padx=20,  # 设置x方向内边距：20
    pady=10 # 设置y方向内边距：10
)

l3.pack()

# 显示出来
window.mainloop()
