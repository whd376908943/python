#!/bin/env python
#-*-coding:utf-8-*-
import jenkins
import time
import sys
from termcolor import colored

url = ''
username = ''
password = ''
job = ''

msg = colored("初始化连接...", 'green')
print msg
server = jenkins.Jenkins(url,username,password)

next_number = server.get_job_info(job)['nextBuildNumber']
msg = colored('本次构建项目编号:{0}'.format(next_number),'green')
print msg


msg = colored("开始构建项目:{0}".format(job), 'green')
print msg
server.build_job(job)
time.sleep(10)

msg = colored("构建开始:",'green')
print msg
while server.get_build_info(job,next_number)['building']:
    print '.',
    time.sleep(1)
    sys.stdout.flush()

build_info = server.get_build_info(job,next_number)
status = build_info['result']

if status == "SUCCESS":
    msg = colored("构建成功!",'green')
    print msg
else:
    msg = colored("构建失败!",'red')
    print msg
