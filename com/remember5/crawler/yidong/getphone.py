import requests
import redis
import smtplib
from email.mime.text import MIMEText
from email.header import Header

r = redis.Redis(host='localhost', port=6379, db=0, password='123456')


def check_phone():
    """
    获取手机号
    """
    url = "https://kapi.10010.com/kcardorder/intentionalOrder/selectNumGuessYouLike"

    phone_num_list = ['0819', '0108']

    payload = "productType=k107&provinceCode=11&cityCode=110&searchValue={}&searchType=02&channel=01-0379-a5j9-a76y&id=5A754562316F72515754486F47416D68683747316834554B33353445496552786869433938625936515279786267475A41566F4B4730696534566345344C5762"

    headers = {
        'Host': 'kapi.10010.com',
        'Cookie': 'acw_tc=7250b39516793003883378781e5d134f11113ef139a54d05f9aea141f6; KSESSIONID=M2M1MDVmMTYtYWEzMS00MTdlLWE5YjctOWE1ZGQyMjUxODI3',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        'origin': 'https://txwk.10010.com',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.6(0x13060011) Safari/605.1.15 NetType/WIFI',
        'referer': 'https://txwk.10010.com/'
    }

    for x in phone_num_list:
        response = requests.request("POST", url, headers=headers, data=payload.format(x))
        rep = response.json()
        if rep['code'] == '20000':
            for d in rep['data']:
                number = d['number']
                r.sadd(x, number)
                if '010819' in number:
                    print("找到，发送邮件")
                    send_email(number)


def send_email(phone=None):
    smtp = "smtp.qq.com"  # smtp
    sender = '1332661444@qq.com'  # 发送的邮箱
    pwd = ''  # 授权密码
    receivers = ['123@qq.com', '1234@qq.com']  # 收信人邮件，可设置为你的QQ邮箱或者其他邮箱

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
    check_phone()
