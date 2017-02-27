# coding:utf-8

import smtplib
from email.mime.text import MIMEText

path = r'C:\Users\wanghuidong\Desktop\VisualSVN-SvnAuthz.ini'

user_filter = [
    'xuewentao',
    'xuejie'
]
project_filter = [
    '/trunk/outside/arch-base',
    '/trunk/outside/arch-base/code',
    '/trunk/outside/arch-base/code/backend_html',
    '/trunk/outside/arch-biz'
]


def get_content(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content


def get_all_project(content):
    project = content.split('\n\n')
    return project[1:]


def filter_project(project):
    line = project.split('\n')
    if line[0].startswith('[/trunk') and line[0][1:-1] not in project_filter:
        return True


def get_project():
    content = get_content(path)
    all_project = get_all_project(content)
    project = filter(filter_project, all_project)
    return project


# 独立
def get_project_res(project):
    user_list = []
    group_list = []
    line = project.split('\n')
    authz_list = line[1:]
    for user_authz in authz_list:
        user, authz = user_authz.split('=')
        if user not in user_filter and authz == 'rw':
            if user.startswith('@'):
                group_list.append(user[1:])
            else:
                user_list.append(user)
    all_user = '--'.join(user_list)
    all_group = '--'.join(group_list)
    if user_list and group_list:
        content = '''<br/>***Project Name:{0}***<br/>
*Write_user:<br/>{1}<br/>*Write_group:<br/>{2}<br/>'''.format(line[0][1:-1], all_user, all_group)
    elif user_list:
        content = '''<br/>***Project Name:{0}***<br/>
*Write_user:<br/>{1}<br/>'''.format(line[0][1:-1], all_user)
    elif group_list:
        content = '''<br/>***Project Name:{0}***<br/>
*Write_group:<br/>{1}<br/>'''.format(line[0][1:-1], all_group)
    else:
        content = ''
    return content


def get_res():
    res = ''
    for project in get_project():
        res = '{0}{1}'.format(res, get_project_res(project))
    return res


class Mail(object):
    def __init__(self):
        self.mail_from = 'monitor@vjwealth.com'
        self.passwd = 'WEI2016jiankongbaojing'
        self.smtp_server = 'smtp.exmail.qq.com'
        self.mail_to = 'wanghuidong@vjwealth.com'

    def wrapper(self, subject):
        self.msg = MIMEText(get_res(), 'html', 'utf-8')
        self.msg['Subject'] = subject
        self.msg['From'] = self.mail_from
        self.msg['To'] = 'wanghuidong@vjwealth.com'

    def mail(self):
        smtp = smtplib.SMTP(self.smtp_server)
        smtp.login(self.mail_from, self.passwd)
        smtp.sendmail(self.mail_from, self.mail_to, self.msg.as_string())


if __name__ == '__main__':
    m = Mail()
    m.wrapper('svn authz')
    m.mail()

