# coding:utf-8


import paramiko

hostname = "192.168.8.2"
username = 'root'
password = '123456'

paramiko.util.log_to_file(r'E:\sys.log')     # 记录日志文件，可有可无
ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()   加载本地的公钥校验文件
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 设置连接的远程主机没有密钥时的策略
ssh.connect(hostname, 22, username, password)
stdin, stdout, stderr = ssh.exec_command("/usr/local/java/jdk1.7.0_67/bin/jmap -h")    # 标准输入，输出，错误
# print stdout.readlines()
print stdout.read()
ssh.close()


'''
# 通过密钥方式登录远程主机
import paramiko
import os

hostname='192.168.189.129'
username='root'

paramiko.util.log_to_file('syslogin.log')
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey = os.path.expanduser('/root/.ssh/id_rsa')            #定义私钥存放路径
key = paramiko.RSAKey.from_private_key_file(privatekey)        #创建私钥对象key
ssh.connect(hostname = hostname, username = username, pkey = key)
stdin, stdout, stderr = ssh.exec_command('ifconfig')
print stdout.read()
ssh.close()

'''


'''
    堡垒机环境在一定程度上提升了运营安全级别，但同时也提高了日常运营成本。
作为管理的中转设备，任何针对业务服务器的管理请求都会经过此节点，比如SSH协议，
首先运维人员在办公电脑通过SSH协议登录堡垒机，再通过堡垒机SSH跳转到所有的业务服务器进行维护操作。
    我们可以利用paramiko的invoke_shell机制来实现通过堡垒机实现服务器操作，
原理是SSHClient.connect到堡垒机后开启一个新的SSH会话(session)，通过新的会话运行“ssh user@IP”去实现远程执行命令的操作。
    具体代码实现参考python自动化运维的paramiko相关模块。
'''
