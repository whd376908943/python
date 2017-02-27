#! coding:utf-8


from fabric.api import *
from fabric.contrib.console import confirm


env.user = 'root'
env.password = 'hadoop'
env.hosts = ['192.168.189.129']


@runs_once
def wrapper_task():
    with lcd('/root'):
        local('tar -cvf demo.xlsx.tar demo.xlsx')


def put_task():
    run('mkdir /xls')
    with lcd('/root'):
        res = put('demo.xlsx.tar', '/xls/demo.xlsx.tar')
    if res.failed and not confirm('put failure, Continue[Y/N]？'):
        abort('put failure')


def check_task():
    with lcd('/root'):
        # 获取本地命令的结果时必须指定capture，否则无法获取到结果
        lmd5 = local('md5sum demo.xlsx.tar', capture=True).split()[0]
    rmd5 = run('md5sum /xls/demo.xlsx.tar').split()[0]
    if lmd5 == rmd5:
        print 'success!'
    else:
        print 'error!'


def deploy():
    wrapper_task()
    put_task()
    check_task()
