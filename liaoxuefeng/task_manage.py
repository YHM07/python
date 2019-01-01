#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import random, time, queue

from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue',  callable=lambda : task_queue)
QueueManager.register('get_result_queue', callable=lambda : result_queue)

# 绑定端口8000，设置验证码'abc'
authkey = b'abc'
manager = QueueManager(address=('',8000), authkey=authkey)

# 启动Queue
manager.start()

# 获得通过网络访问的Queue对象
task   = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for index in range(10):
    n = random.randint(0,100)
    print('put task {0}..'.format(n))
    task.put(n)

# 从result队列读取结果 
for index in range(10):
    r = result.get(timeout = 10)
    print('Result: {0}'.format(r))

# 关闭
manager.shutdown()
print('master exit')

