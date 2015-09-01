#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManger:
class QueueManger(BaseManager):
    pass

# 由于这个QueueManger只从网络上获取Queue，所以注册时只需提供名字
QueueManger.register('get_task_queue')
QueueManger.register('get_result_queue')

# 链接到服务器，也就是运行task_master.py的机器
server_addr = '127.0.0.1'
print('Connect to server {0}'.format(server_addr))

# 端口和验证码保持task_master.py设置的完全一致
authkey = b'abc'
m = QueueManger(address=(server_addr, 8000), authkey = authkey)

# 从网络连接
m.connect()

# 获取queue对象
task   = m.get_task_queue()
result = m.get_result_queue()

# 从task队列获取任务，并把结果写入result队列
for index in range(10):
    try:
        n = task.get(timeout=5)
        print('run task {0} * {1}...'.format(n,n))
        r = '{0} * {1} = {2}'.format(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')

# 处理结束
print('worker exit')
