# coding:utf-8
import urllib
import re
import smtplib
from email.mime.text import MIMEText
from random import randint


def html(url):
    f = urllib.urlopen(url)
    res = f.read().decode('gbk').encode('utf-8')
    return res


def content(html):
    pattern = re.compile('\d+、(.*)</p>')
    list = pattern.findall(html)
    return list


class Mail(object):
    def __init__(self):
        self.mail_from = 'wanghuidong@cmcaifu.com'
        self.passwd = 'qwe123!'
        self.smtp_server = 'mail.cmcaifu.com'
        # self.mail_to = ['wanghd.dlc@outlook.com', '376908943@qq.com']
        self.mail_to = '376908943@qq.com'

    def wrapper(self, subject, ls):
        content = ls[randint(0, len(ls)-1)]
        self.msg = MIMEText(content, 'html', 'utf-8')
        self.msg['Subject'] = subject
        self.msg['From'] = self.mail_from
        # self.msg['To'] = ','.join(self.mail_to)
        self.msg['To'] = '376908943@qq.com'

    def mail(self):
        smtp = smtplib.SMTP(self.smtp_server)
        smtp.login(self.mail_from, self.passwd)
        smtp.sendmail(self.mail_from, self.mail_to, self.msg.as_string())

h = html('http://www.cnrencai.com/jiyu/423819.html')
ls = content(h)
m = Mail()
m.wrapper('My Congraulation!', ls)
m.mail()
