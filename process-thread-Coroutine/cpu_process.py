import time
from  multiprocessing import Process
import os


def hello(num):
    while True:
        num += 1
        print(f'{os.getpid()}-{num}')
        if(num == 5000000):
            break

for i in range(2):
    t = Process(target=hello,args=(i,))
    t.start()



print('process end')
