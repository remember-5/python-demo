import time

import requests
from concurrent.futures import ThreadPoolExecutor  # 线程池，进程池


# lwy抢床位，结果没成功

class QiangPiao:
    """
    1. 安装python
    2. 安装request库 执行'pip install requests'
    """

    def __init__(self):
        self.username = "2131141212"
        self.password = "310104200008220025"
        self.login_url = "https://enroll.gench.edu.cn/api/stu/login"
        self.set_dorm_url = "https://enroll.gench.edu.cn/api/stu/set_dorm"
        self.cookies = None

    def login(self):
        print("开始登录")
        data = {
            'enrollid': self.username,
            'idcard': self.password
        }
        res = requests.post(self.login_url, data=data)
        if res.status_code == 200:
            print("登录成功")
            cookie = requests.utils.dict_from_cookiejar(res.cookies)
            print("cookie=", cookie)
            self.cookies = cookie

    def set_room(self, name):
        # 4代表的是房间号，已在网页查看
        data = {
            'did': 4
        }
        while True:
            res = requests.post(self.set_dorm_url, cookies=self.cookies, data=data)
            if res.status_code == 200:
                print("开始抢房间,当前线程:", name, res.json(), "==========================")


if __name__ == '__main__':
    qp = QiangPiao()
    qp.login()
    pool = ThreadPoolExecutor(6)
    for i in range(1, 7):
        pool.submit(qp.set_room, "Thread" + str(i))
