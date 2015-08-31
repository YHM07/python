#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import threading
import random
import time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        wait_time = random.randrange(1,10)
        print('{0} will wait {1} seconds'.format(self.name, wait_time))
        time.sleep(wait_time)
        print('{0} finished'.format(self.name))

if __name__ == '__main__':

    print('main Thread is waiting for exit...')
    for i in range(5):
        t = MyThread()
        t.setDaemon(True)
        t.start()

    print('main thread finished')
