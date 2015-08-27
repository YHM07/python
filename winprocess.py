#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''multiprocessing process'''

__author__ = 'H.M.Yang'

from multiprocessing import Process
import os

# the code will be did by child process
def run_proc(*args):
    print 'Run child process %s (%s)...' % (args[0],os.getpid())
    print 'args is %s' % (args[1])
if __name__ == '__main__':
    print 'Parent process %s.' % (os.getpid())
    p = Process(target=run_proc,args=(('test','Hello')))
    print 'Process will start'
    p.start()
    p.join()
    print 'process end'
