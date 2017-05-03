# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from random import randint


class Mail(object):
    def __init__(self):
        self.mail_from = '*********'
        self.passwd = '*****'
        self.smtp_server = '********'
        # self.mail_to = ['******', '******']
        self.mail_to = '359274291@qq.com'

    def wrapper(self, subject):
        str = 'abcdefghijklmnopqrstuvwxyz'
        content = str[randint(0, 25)]
        self.msg = MIMEText(content, 'html', 'utf-8')
        self.msg['Subject'] = subject
        self.msg['From'] = self.mail_from
        # self.msg['To'] = ','.join(self.mail_to)
        self.msg['To'] = '359274291@qq.com'

    def mail(self):
        smtp = smtplib.SMTP(self.smtp_server)
        smtp.login(self.mail_from, self.passwd)
        smtp.sendmail(self.mail_from, self.mail_to, self.msg.as_string())


m = Mail()
m.wrapper('only run to test')
m.mail()
