# coding:utf-8


import os
import time


svnproject = ['doc', 'project']


def backup(svn):
    os.system('net stop "VisualSVN Server"')
    for project in svn:
        os.system('svnadmin dump D:\\Repositories\\{0} > D:\\svn_back\\{0}.{1}.dump'.format(project, time.strftime('%Y-%m-%d')))
    os.system('net start "VisualSVN Server"')


def delete():
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()-30*24*60*60))
    back_file = os.listdir('D:\\svn_back')
    for back in back_file:
        date = back.split('.')[1]
        if date < day:
            os.remove('D:\\svn_back\\{0}'.format(back))


if __name__ == '__main__':
    backup(svnproject)
    delete()



