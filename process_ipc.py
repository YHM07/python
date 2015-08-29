#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

from multiprocessing import Process, Queue

import os, time, random

# write to Queue
def write(q):
    print('Process to write: {0}'.format(os.getpid()))
    for val in ['a','b','c']:
        print('puts {0} to queue'.format(val))
        q.put(val)
        time.sleep(random.random())

# read from Queue
def read(q):
    print('Process to read: {0}'.format(os.getpid()))
    while(True):
        val = q.get()
        print('Get {0} from Queue'.format(val))

if __name__ == '__main__':
# 父进程创建Queue，并传给各个子进程
    queue = Queue()
    pw = Process(target=write, args=(queue,))
    pr = Process(target=read , args=(queue,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

