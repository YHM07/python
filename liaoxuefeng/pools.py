#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''pool'''

__author__ = 'H.M.Yang'

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name,os.getpid())
    # start = time.time()
    # time.sleep(random.randint() * 3)
    # end = time.time()
    # print 'Task %s run %2.2f seconds.' % (name,(end - start))
    print 'Task %s done.' % name
    
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done'
