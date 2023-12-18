# coding=utf-8
import sys
import re
import requests
from requests.exceptions import MissingSchema
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog

import qt1

####################### 全局变量#########################
app = QApplication(sys.argv)


class MyWindows(qt1.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)


my_windows = MyWindows()  # 实例化对象
my_windows.show()  # 显示窗口

pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
copy_url = ''
save_path = ''


def download(url, play_id):
    try:
        r = requests.get(url, stream=True)
        with open('{}/{}.mp4'.format(save_path, play_id), "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)
        msg_box = QMessageBox(QMessageBox.NoIcon, '提示', '下载完成!')
        msg_box.exec_()
    except (BaseException, MissingSchema) as e:
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '下载失败!')
        msg_box.exec_()


def get_real_download_url(base_url):
    try:
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
    except (MissingSchema) as e:
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '地址不正确哦,换个链接试试')
        msg_box.exec_()
        return None, None


####################### button click #########################


def download_btn_click():
    """
    点击下载链接
    """
    url, play_id = real_url_btn_click()
    if url is not None and play_id is not None:
        if save_path is None or save_path == '':
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '请先设置保存路径!')
            msg_box.exec_()
        else:
            download(url, play_id)


def real_url_btn_click():
    """
    获取真实链接
    """
    input_url = my_windows.share_url.text()
    if input_url is not None and "" != input_url and len(input_url) != 0:
        # 正则处理一下url
        if len(pattern.findall(input_url)) > 0:
            input_url = pattern.findall(input_url)[0]
            url, play_id = get_real_download_url(input_url)
            my_windows.real_url.setText(url)
            global copy_url
            copy_url = url
            return url, play_id
        else:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '未匹配到URL')
            msg_box.exec_()
            return None, None
    else:
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '需要给我个链接才能转换哦')
        msg_box.exec_()
        return None, None


def copy_btn_click():
    """
    复制链接
    """
    clipboard = QApplication.clipboard()
    clipboard.setText(copy_url)


def save_path_click():
    """
    选择文件夹
    """
    global save_path
    save_path = QFileDialog.getExistingDirectory(my_windows, "选择文件夹", "/")
    my_windows.savePathTextBrowser.setText(save_path)


my_windows.download_btn.clicked.connect(download_btn_click)
my_windows.real_url_btn.clicked.connect(real_url_btn_click)
my_windows.copy_btn.clicked.connect(copy_btn_click)
my_windows.save_path_btn.clicked.connect(save_path_click)

sys.exit(app.exec_())
