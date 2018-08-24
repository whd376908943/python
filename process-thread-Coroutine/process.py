import time
from multiprocessing import Process
import os
# 多进程平均30s

def hello():
    print('Hello world! (%s)' % os.getpid())
    time.sleep(30)
    print('Hello again! (%s)' % os.getpid())

for i in range(2):
    t = Process(target=hello,name=f'process-{i}')
    t.start()

print('end')
