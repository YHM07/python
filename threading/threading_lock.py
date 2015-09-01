#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import threading
import time
count = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        global mutex
        time.sleep(1)
        if mutex.acquire():
            count += 1
            msg = self.name + ' set count to ' + str(count)
            print(msg)
            mutex.release()

if __name__ == '__main__':

    for i in range(5):
        t = MyThread()
        t.start()



