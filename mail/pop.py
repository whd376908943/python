# -*- coding:utf-8 -*-

import poplib
from pprint import pprint
import time
from base64 import b64decode
import xlwt

# 填写个人邮箱及密码
host = 'pop.263.net'
user = ''
password = ''

workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('mail')
# 为了使表格可以插入汉字
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'SimSun'
style.font = font

p = poplib.POP3(host)
p.set_debuglevel(1)
p.user(user)
p.pass_(password)
# ret = p.stat()
# print ret

# res = p.list()
# print res
'''
down = p.retr(1071)

for line in down[1]:
    print line
'''


def filter_subject(string):
    if string.startswith('Subject'):
        return True


def filter_date(string):
    if string.startswith('Date'):
        return True


def filter_from(string):
    if string.startswith('From'):
        return True


def get_subject(num):
    string = filter(filter_subject, p.top(num, 0)[1])[0]
    if 'gb2312' in string:
        return b64decode(string.split('?')[-2]).decode('gbk').encode('utf-8')
    elif 'GB2312' in string:
        return b64decode(string.split('?')[-2]).decode('gbk').encode('utf-8')
    elif 'utf' in string:
        return b64decode(string.split('?')[-2])
    elif 'UTF' in string:
        return b64decode(string.split('?')[-2])
    else:
        return string.split(':')[-1].strip()


def get_date(num):
    tim = filter(filter_date, p.top(num, 0)[1])[0]
    date = tim.split('+')[0].split(',')[-1].strip()
    res_date = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(date, '%d %b %Y %X'))
    return res_date


def get_from(num):
    mail_from = filter(filter_from, p.top(num, 0)[1])[0]
    res = mail_from.split('<')[-1][:-1]
    if 'From' in res:
        return res.split(':')[-1].strip()
    return res


for num in range(1, p.stat()[0]+1):
    if 'monitor' in get_from(num):
        continue
    if num == 1004:
        continue
    sheet.write(num, 0, get_from(num))
    sheet.write(num, 1, get_subject(num))
    sheet.write(num, 2, get_date(num))

workbook.save(r'E:\mail.xls')
# pprint(p.top(304, 0))
# print get_from(304)

p.quit()

