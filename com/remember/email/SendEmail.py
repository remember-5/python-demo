import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == '__main__':
    smtp = "smtp.qq.com"  # smtp
    sender = '1332661444@qq.com'  # 发送的邮箱
    pwd = 'xxx'  # 授权密码
    receivers = ['1332661444@qq.com']  # 收信人邮件，可设置为你的QQ邮箱或者其他邮箱

    # 这里是body的内容
    mail_msg = """
    <p>Python 通知</p>
    <p><a href="http://www.baidu.com">找到手机号了</a></p>
    """

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = ".".join(receivers)

    # 这是标题
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(smtp, 465)
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
