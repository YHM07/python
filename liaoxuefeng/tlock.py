#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import time,threading

balance = 0
lock = threading.Lock()

def change(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(i)
        finally:
            lock.release()
if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread,args=(5,))
    t2 = threading.Thread(target=run_thread,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print balance

