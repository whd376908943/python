import time
import threading


# 多线程平均30s

def hello():
    print('Hello world! (%s)' % threading.currentThread())
    time.sleep(30)
    print('Hello again! (%s)' % threading.currentThread())

for i in range(2):
    t = threading.Thread(target=hello)
    t.start()

print('end')
