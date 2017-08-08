#encoding=utf-8;

import os;
import time,threading

# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
#
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

balance = 0
lock = threading.Lock()

def chance_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # print("%s" %threading.current_thread().name)
        # 获得锁
        lock.acquire()
        try:
            chance_it(n)
        finally:
            # 释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,) , name= "t1")
t2 = threading.Thread(target=run_thread, args=(8,) , name= "t2")
t1.start()
t2.start()
# t1,t2开始执行，遇到tx.join后，会让子线程将t1的target执行完后再走主线程后的代码
t1.join()
print("t1prite")
t2.join()
print("t2prite")
print(balance)