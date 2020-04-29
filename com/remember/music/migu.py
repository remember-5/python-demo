import json
import os
import requests
import time
import xlrd
import xlwt

from selenium import webdriver

def run():
    # 先打开chromedriver
    driver = webdriver.Chrome()

    # 打开播放器
    player_url = 'http://music.migu.cn/v3/music/player/audio'
    driver.get(player_url)
    # 定位当前页面句柄
    player_index = driver.current_window_handle
    print('player_index = ', player_index)

    # 打开所有页面
    jay_url = 'http://music.migu.cn/v3/music/artist/112/song?page='
    for i in range(1, 17):
        page_url = jay_url + str(i)
        js = f"window.open('{page_url}')"
        driver.execute_script(js)

    # 获取全部页面句柄
    all_handles = driver.window_handles
    print('all_handles=', all_handles)

    # 遍历全部页面句柄
    for i in range(1, 17):
        handle = all_handles[i]
        # 切换到新页面
        driver.switch_to.window(handle)
        print('now_handles=', driver.current_window_handle)

        # 开始处理点击事件
        song_list = driver.find_elements_by_class_name('song-play')
        for song in song_list:
            song.click()
            time.sleep(2)
    time.sleep(600)


def download_music():
    excel_path = '/Users/wang/Desktop/周杰伦.xlsx'
    download_path = '/Volumes/电影/音乐/周杰伦/'

    workbook = xlrd.open_workbook(excel_path)

    sheet = workbook.sheet_by_name('下载')
    for x in range(1, sheet.nrows):
        rows = sheet.row_values(x)  # 获取第四行内容
        music_name = rows[0]
        url = rows[2]
        # request.urlretrieve(url, download_path + music_name + '.mp3')
        res = requests.get(url)

        with open(download_path + str(music_name) + '.mp3', 'ab') as file:  # 保存到本地的文件名
            file.write(res.content)
            file.flush()

        # cols = sheet.col_values(1)  # 获取第二列内容
        print(rows)


def write_excel(data):
    print(len(data))
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    a = 0
    for d in data:
        i = 0
        for k in d['sqPlayInfo']:
            sheet.write(a, i, k)  # 第0行第一列写入内容
            i += 1
        a += 1

    wbk.save('/Users/wang/Desktop/server/wangjiahao/charlesLog/test.xls')


def read_file():
    all_data = []
    file_path = '/Users/wang/Desktop/server/wangjiahao/charlesLog/audioPlayer/'
    # 处理数据
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.startswith('getPlayInfo'):
                with open(file_path + file, encoding='utf-8') as file_obj:
                    js = json.loads(file_obj.read())
                    if 'data' in js:
                        data = js['data']
                        result = dispose_data(data)
                        all_data.append(result)
    write_excel(all_data)


def dispose_data(data):
    result = {}
    # bqPlayInfo hqPlayInfo sqPlayInfo 下面的playUrl就是播放地址
    url = 'playUrl'
    url_list = []
    for (k, v) in data.items():
        if k is None or v is None:
            pass
        else:
            for (q, p) in v.items():
                if q is None or p is None:
                    pass
                else:
                    if url == q:
                        url_list.append(p)
    result[k] = url_list
    return result


if __name__ == '__main__':
    run()
    # read_file()
    # download_music()
