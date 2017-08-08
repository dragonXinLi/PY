#encoding=utf-8;

import os;
import time,threading

def loop():
    print("prite %s is running..." %threading.current_thread().name)
    n = 0
    while n <5:
        n = n+1
        print("thread %s >>> %s" % (threading.current_thread().name , n))
        time.sleep(1)
    print("thread %s ended " %threading.current_thread().name)

print("thread %s is running..." % threading.current_thread().name)
# t = threading.Thread(target=loop(), name= 'LoopThread') loop()直接执行了,
t = threading.Thread(target=loop, name= 'LoopThread')
t.start()
t.join()
print("thread %s ended" %threading.current_thread().name)
