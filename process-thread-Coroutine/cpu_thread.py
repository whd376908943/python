import time
import threading


def hello(num):
    while True:
        num += 1
        print(f'{threading.currentThread().name}-{num}')
        if(num == 5000000):
            break

for i in range(2):
    t = threading.Thread(target=hello,args=(i,))
    t.start()
    



print('end')
