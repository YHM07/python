#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''multiprocessing'''

__author__ = 'H.M.Yang'

import os

def pro():
    print 'Process (%s) start...'  % os.getpid()
    pid = os.fork()
    if pid == 0:
        print 'I am child Process (%s) and my parent is %s.' % (os.getpid(),os.getppid())
    else:
        print 'I (%s) just created a child Process (%s).' % (os.getpid(),pid)
if __name__  == '__main__':
    pro()
