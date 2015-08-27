#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

from multiprocessing import Process, Queue
import os,time,random

# write Process
def write(q):
    print 'write Process %s ' % os.getpid()
    for value in ['A','B','C']:
        print 'Put %s to Queue...' % value
        q.put(value)
        time.sleep(random.random())
# read Process
def read(q):
    print 'read Process %s ' % os.getpid()
    while True:
        value = q.get(True)
        print 'Get %s from Queue' % value

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
