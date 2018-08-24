import os
import json
from threading import Thread

def hello(num):
    with open(f'/tmp/thread-{num}.txt','w') as f:
        json.dump(list(range(50000000)),f)

for i in range(2):
    t = Thread(target=hello,args=(i,))
    t.start()



print('thread end')
