#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
进程a创建后共享父进程程序代码，如果后续继续创建子进程，那么a子进程同样会创建新的子进程
"""
__author__ = 'H.M.Yang'

import os

print('Process {0} start...'.format(os.getpid()))
pid = os.fork()
if pid == 0:
    print("i am child Process {0} and my parent is {1}".format(os.getpid(), os.getppid()))
else:
    print('i {0} just creat Process {1}'.format(os.getpid(), pid))


from multiprocessing import Process

# 子进程要执行的代码
def run_pro(name):
    print('Run child Process {0} ({1}) and my parent Process {2}'.format(name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    print('Parent Process {0} '.format(os.getpid()))
    p = Process(target=run_pro, args=('test',))
    print('child Process will start')
    p.start()
    p.join()
    print('chile Process end')

