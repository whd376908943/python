import time
from  multiprocessing import Process
import os
import json

def hello(num):
    with open(f'/tmp/process-{num}.txt','w') as f:
        json.dump(list(range(50000000)),f)

for i in range(2):
    t = Process(target=hello,args=(i,))
    t.start()



print('process end')
