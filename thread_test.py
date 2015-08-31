#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import time, threading

def loop():
    """TODO: Docstring for loop.
    :returns: TODO

    """
    print('thread {0} is running'.format(threading.current_thread().name))
    for n in range(1,5):
        print('thread {0} >>> {1}'.format(threading.current_thread().name,n))
        time.sleep(1)
    print('thread {0} ended'.format(threading.current_thread().name))
    
print('thread {0} is running'.format(threading.current_thread().name))
t = threading.Thread(target=loop)
t.start()
t.join()
print('thread {0} ended'.format(threading.current_thread().name))

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire() 
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)

local_school = threading.local()

def process_student():
    std = local_school.student
    print('hello {0} (in {1})'.format(std, threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',))
t2 = threading.Thread(target=process_thread, args=('Bob',))

t1.start()
t2.start()
 
t1.join()
t2.join()

