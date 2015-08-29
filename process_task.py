#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

"""
Python多进程模块Multiprocessing介绍
"""
import multiprocessing as mul 
import os
from math import factorial

def get_factorial(num, pid = 0):
    if pid:
        print('pid is {0}'.format(os.getpid()))
    return factorial(num)

f_10 = get_factorial(10, pid=1)

def f_list_serial(num, pid=0):
    results = []
    for i in range(1,num+1):
        results.append(get_factorial(i,pid=pid))
    return results

results = f_list_serial(5,pid=1)

f_100 = f_list_serial(100, pid=0)

def f_list_para_apply_async(num, pid=0, pool=None):
    pool = mul.Pool(4)
    results = []
    results_list = []
    for i in range(1,num+1):
        results_list.append(
                pool.apply_async(get_factorial, args=(i,pid)))
    pool.close()
    pool.join()
    for result in results_list:
        results.append(result.get())
    return results

r = f_list_para_apply_async(10, pid=1)

