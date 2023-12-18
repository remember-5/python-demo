#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = ''
receivers = []
subject = ''
body = ''
code = ''
smtp = ""
parser = argparse.ArgumentParser(description='帮助描述信息', prog='程序显示名称', usage='顶部显示信息，会覆盖prog',
                                 epilog='底部显示信息')  ## 括号里面可以什么都不写，会走默认
parser.add_argument('-sender', '--sender', dest='sender', type=str, help='发送方邮箱')
parser.add_argument('-receivers', '--receivers', dest='receivers', nargs='*', type=str, help='接收方，可同时发送至多个接受方')
parser.add_argument('-subject', '--subject', dest='subject', type=str, help='标题')
parser.add_argument('-body', '--body', dest='body', type=str, help='需要发送的内容')
parser.add_argument('-code', '--code', dest='code', type=str, help='授权码')
parser.add_argument('-smtp', '--smtp', dest='smtp', type=str, help='smtp地址')


def sendEmail(sender, receivers, subject, body, code):
    """
    发送邮件
    :param sender: sender(string):发送方
    :param receivers: receivers(string数组):接收方，可同时发送至多个接受方
    :param subject: subject(string):标题
    :param body: body(string):需要发送的内容
    :param code: code(string):授权码
    :return: noting
    """
    for receiver in receivers:
        msgRoot = MIMEText(body, 'html', 'utf-8')
        msgRoot['From'] = Header(sender)
        msgRoot['To'] = Header(receiver)
        msgRoot['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(host=smtp, port=25)
            smtpObj.login(sender, code)
            smtpObj.sendmail(sender, receiver, msgRoot.as_string())
            print(receiver, "邮件发送成功")
        except smtplib.SMTPException as exp:
            print(receiver, "Error: 无法发送邮件", exp)


if __name__ == '__main__':
    # 此处支持自定义脚本参数
    args = parser.parse_args()
    # print(args)
    sender = args.sender
    receivers = args.receivers
    subject = args.subject
    body = args.body
    code = args.code
    smtp = args.smtp

    print('sender', sender)
    print('receivers', receivers)
    print('subject', subject)
    print('body', body)
    print('code', code)
    print('smtp', smtp)
    sendEmail(sender, receivers, subject, body, code)
