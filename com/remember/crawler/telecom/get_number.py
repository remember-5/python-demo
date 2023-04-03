# import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import redis

# import sqlite_utils
import requests

# db = sqlite_utils.Database("my.db")
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')


# def init_table():
#     if db["telecom_number"].exists() is False:
#         db.execute("""
#         create table telecom_number
#         (
#             number TEXT
#         );
#         """)
#         db.execute("""
#         create unique index telecom_number_number_uindex on telecom_number (number)
#         """)


def get_number():
    url = "https://act.aisulin.cn/activity/getnumber"

    payload = '{"cid":"1","type":"1","page":1,"pageSize":"10000"}'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Cookie': 'JSESSIONID=35E5A5399BF22BFDB895F5A836195BAF',
        'Origin': 'https://act.aisulin.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://act.aisulin.cn/activity/savecardOrder?cid=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        for x in response.json()['data']:
            try:
                number = x['number']
                # db['telecom_number'].insert({
                #     'number': number
                # })
                r.sadd('telecom_number', number)
            except Exception:
                print('号码已经存在', number)
                pass


def send_email(phone):
    smtp = "smtp.qq.com"  # smtp
    sender = '1332661444@qq.com'  # 发送的邮箱
    pwd = 'xxx'  # 授权密码
    receivers = ['xxx@qq.com', 'xxx@qq.com']  # 收信人邮件，可设置为你的QQ邮箱或者其他邮箱

    # 这里是body的内容
    mail_msg = """
            <p>Python 邮件通知</p>
            <p>找到手机号了{}</p>
            """.format(phone)

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receivers)

    # 这是标题
    subject = '消息提醒'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(smtp, 465)
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    # init_table()
    get_number()
    # for x in range(100):
    #     get_number()
    #     time.sleep(5)
