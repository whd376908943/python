import time
import threading

def hello():
    print('Hello world! (%s)' % threading.currentThread())
    time.sleep(30)
    print('Hello again! (%s)' % threading.currentThread())




for i in range(2):
    hello()
