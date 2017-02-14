##########
# coding:utf-8

from __future__ import division
from fabric.api import *
import MySQLdb
import time
from smtplib import *
from email.mime.text import MIMEText

env.user = 'root'
env.password = '123456'
# 使用passwords选项时必须指定账号和连接端口
# env.passwords = {
#     'root@192.168.189.128:22': 'hadoop',
#     'root@192.168.189.129:22': 'hadoop'
# }
env.roledefs = {
    'web1': ['192.168.8.2'],
    'web2': ['192.168.8.3'],
    'server1': ['192.168.8.4'],
    'server2': ['192.168.8.5']
}


def get_info(tomcat):
    cmd = 'ps aux | grep {0} | grep -v grep'.format(tomcat)
    info = run(cmd)
    return info


def get_cpuinfo(tomcat):
    cpuinfo = get_info(tomcat).split()[2]
    return cpuinfo


def get_meminfo(tomcat):
    meminfo = get_info(tomcat).split()[3]
    return meminfo


def get_generation(tomcat):
    pid = get_info(tomcat).split()[1]
    cmd = 'jmap -heap {0} | grep used | sed -n "0~2p" '.format(pid)
    generation = run(cmd)
    Eden_Space = generation.split('\n')[-5].split()[-2][:-1]
    From_Space = generation.split('\n')[-4].split()[-2][:-1]
    To_Space = generation.split('\n')[-3].split()[-2][:-1]
    PS_Old_Generation = generation.split('\n')[-2].split()[-2][:-1]
    PS_Perm_Generation = generation.split('\n')[-1].split()[-2][:-1]
    generation = [Eden_Space, From_Space, To_Space, PS_Old_Generation, PS_Perm_Generation]
    return generation


def get_host_info():
    cmd = "top -bi -n 2 -d 0.1 | grep Cpu | tail -1 | awk '{print $2}' | awk -F% '{print $1}'"
    cpu = run(cmd)
    mem_total = run("free -m | grep Mem | awk '{print $2}'")
    mem_used = run("free -m | grep Mem | awk '{print $3}'")
    mem = round(float(mem_used) / float(mem_total), 2) * 100
    return cpu, mem


def get_tomcat_parallel(tomcat):
    port = tomcat.split('_')[-1]
    cmd = ' netstat -na | grep {0} | grep ESTAB | wc -l'.format(port)
    tomcat_parallel = run(cmd)
    return tomcat_parallel


def get_httpd_parallel():
    cmd = 'netstat -na | grep 80 | grep ESTAB | wc -l'
    httpd_parallel = run(cmd)
    return httpd_parallel


def get_zookeeper_parallel():
    cmd = 'netstat -na | grep 8590 | grep ESTAB | wc -l'
    httpd_parallel = run(cmd)
    return httpd_parallel


def get_mysql(server_ip):
    conn = MySQLdb.connect(host='192.168.8.6', user='root', passwd='123456', db='oper_db', port=3308)
    cur = conn.cursor()
    sql = 'select distinct(project) from path where ip=%s and status=1'
    parameters = (server_ip,)
    cur.execute(sql, parameters)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def insert_mysql(sql, parameters):
    conn = MySQLdb.connect(host='192.168.8.6', user='root', passwd='123456', db='oper_db', port=3308)
    cursor = conn.cursor()
    cursor.execute(sql, parameters)
    conn.commit()
    cursor.close()
    conn.close()


def mail(content):
    from_address = 'monitor@vjwealth.com'
    to_address = ['yunwei@vjwealth.com']
    server = 'smtp.exmail.qq.com'
    passwd = 'WEI2016jiankongbaojing'
    subject = u'tomcat新老生代报警'
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_address

    server = SMTP(server, 25)
    server.login(from_address, passwd)
    server.sendmail(from_address, to_address, msg.as_string())


def compare(tomcat, Eden_Space, PS_Old_Generation):
    if float(Eden_Space) < 1:
        mail("project {0}'s   Eden_Space  is {1}".format(tomcat[0], Eden_Space))
    elif float(Eden_Space) > 90  and  float(PS_Old_Generation) > 95:
        mail("project {0}'s   Eden_Space  is {1}  and  PS_Old_Generation is {2}".format(tomcat[0], Eden_Space, PS_Old_Generation))

@task
@roles('web1')
def execute_sql_web1():
    sql = 'insert into info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    for tomcat in get_mysql(env.roledefs['web1'][0]):
        generation = get_generation(tomcat[0])
        compare(tomcat, generation[0], generation[3])
        tomcat_parameters = (env.roledefs['web1'][0], tomcat[0], get_cpuinfo(tomcat[0]), get_meminfo(tomcat[0]),
                             get_tomcat_parallel(tomcat[0]), time.strftime('%Y-%m-%d %H:%M:%S'),
                             generation[0], generation[1], generation[2],
                             generation[3], generation[4])
        insert_mysql(sql, tomcat_parameters)
    httpd_parameters = (
    env.roledefs['web1'][0], 'httpd', None, None, get_httpd_parallel(), time.strftime('%Y-%m-%d %H:%M:%S'), None, None,
    None, None, None)
    insert_mysql(sql, httpd_parameters)
    host_parameters = (
    env.roledefs['web1'][0], 'host', get_host_info()[0], get_host_info()[1], None, time.strftime('%Y-%m-%d %H:%M:%S'),
    None, None, None, None, None)
    insert_mysql(sql, host_parameters)


@task
@roles('web2')
def execute_sql_web2():
    sql = 'insert into info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    for tomcat in get_mysql(env.roledefs['web2'][0]):
        generation = get_generation(tomcat[0])
        compare(tomcat, generation[0], generation[3])
        tomcat_parameters = (env.roledefs['web2'][0], tomcat[0], get_cpuinfo(tomcat[0]), get_meminfo(tomcat[0]),
                             get_tomcat_parallel(tomcat[0]), time.strftime('%Y-%m-%d %H:%M:%S'),
                             generation[0], generation[1], generation[2],
                             generation[3], generation[4])
        insert_mysql(sql, tomcat_parameters)
    httpd_parameters = (
    env.roledefs['web2'][0], 'httpd', None, None, get_httpd_parallel(), time.strftime('%Y-%m-%d %H:%M:%S'), None, None,
    None, None, None)
    insert_mysql(sql, httpd_parameters)
    host_parameters = (
    env.roledefs['web2'][0], 'host', get_host_info()[0], get_host_info()[1], None, time.strftime('%Y-%m-%d %H:%M:%S'),
    None, None, None, None, None)
    insert_mysql(sql, host_parameters)


@task
@roles('server1')
def execute_sql_server1():
    sql = 'insert into info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    for tomcat in get_mysql(env.roledefs['server1'][0]):
        generation = get_generation(tomcat[0])
        compare(tomcat, generation[0], generation[3])
        tomcat_parameters = (env.roledefs['server1'][0], tomcat[0], get_cpuinfo(tomcat[0]), get_meminfo(tomcat[0]),
                             get_tomcat_parallel(tomcat[0]), time.strftime('%Y-%m-%d %H:%M:%S'),
                             generation[0], generation[1], generation[2],
                             generation[3], generation[4])
        insert_mysql(sql, tomcat_parameters)
    httpd_parameters = (
    env.roledefs['server1'][0], 'httpd', None, None, get_httpd_parallel(), time.strftime('%Y-%m-%d %H:%M:%S'), None,
    None, None, None, None)
    insert_mysql(sql, httpd_parameters)
    host_parameters = (env.roledefs['server1'][0], 'host', get_host_info()[0], get_host_info()[1], None,
                       time.strftime('%Y-%m-%d %H:%M:%S'), None, None, None, None, None)
    insert_mysql(sql, host_parameters)


@task
@roles('server2')
def execute_sql_server2():
    sql = 'insert into info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    for tomcat in get_mysql(env.roledefs['server2'][0]):
        generation = get_generation(tomcat[0])
        compare(tomcat, generation[0], generation[3])
        tomcat_parameters = (env.roledefs['server2'][0], tomcat[0], get_cpuinfo(tomcat[0]), get_meminfo(tomcat[0]),
                             get_tomcat_parallel(tomcat[0]), time.strftime('%Y-%m-%d %H:%M:%S'),
                             generation[0], generation[1], generation[2],
                             generation[3], generation[4])
        insert_mysql(sql, tomcat_parameters)
    httpd_parameters = (
    env.roledefs['server2'][0], 'httpd', None, None, get_httpd_parallel(), time.strftime('%Y-%m-%d %H:%M:%S'), None,
    None, None, None, None)
    insert_mysql(sql, httpd_parameters)
    zookeeper_parameters = (env.roledefs['server2'][0], 'zookeeper', get_cpuinfo('zookeeper'), get_meminfo('zookeeper'),
                            get_zookeeper_parallel(), time.strftime('%Y-%m-%d %H:%M:%S'), None, None, None, None, None)
    insert_mysql(sql, zookeeper_parameters)
    host_parameters = (env.roledefs['server2'][0], 'host', get_host_info()[0], get_host_info()[1], None,
                       time.strftime('%Y-%m-%d %H:%M:%S'), None, None, None, None, None)
    insert_mysql(sql, host_parameters)


@task
def write_data():
    execute(execute_sql_web1)
    execute(execute_sql_web2)
    execute(execute_sql_server1)
    execute(execute_sql_server2)



