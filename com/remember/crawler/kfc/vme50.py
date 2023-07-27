import smtplib
from email.mime.text import MIMEText
from email.header import Header

import sqlite_utils


def send_email(content):
    smtp = "smtp.qq.com"  # smtp
    sender = 'xxx@qq.com'  # 发送的邮箱
    pwd = 'xxx'  # 授权密码
    receivers = ['xxx@163.com', 'xxx@qq.com']  # 收信人邮件，可设置为你的QQ邮箱或者其他邮箱

    # 这里是body的内容
    mail_msg = """
            <p>{}</p>
            """.format(content)

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receivers)

    # 这是标题
    subject = '疯狂星期四!!!'
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
    db = sqlite_utils.Database("kfc.db")
    content = db.execute("SELECT * FROM kfc ORDER BY RANDOM() LIMIT 1;")
    item = content.fetchone()
    content = item[1]
    print(content)
    send_email(content)
    db.close()
