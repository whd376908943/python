#!/usr/bin/python
# coding:utf-8

import pexpect
import sys

child = pexpect.spawn('ssh -p 16861 lsug@172.16.2.175')
# f = open('/root/expect.log','w')
# child.logfile = f
child.expect('(yes/no)?')
child.sendline('yes')
child.expect('password:')
child.sendline('qa@0506')
child.expect('$')
child.sendline('df -Th')
child.sendline('exit')
# child.interact()
child.close()
# f.close()
