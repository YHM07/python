#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import threading
import time

from queue import Queue

queue = Queue()

class Producer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(seld):
        global queue
        count = 0

        while True:
            for i in range(20):
                if queue.qsize() > 1000:
                    pass
                else:
                    count += 1
                    msg = 'products ' + str(count)
                    queue.put(msg)
                    print(msg)
                time.sleep(1)

class Consumer(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global queue
        while True:
            for i in range(3):
                if queue.qsize() < 100:
                    pass
                else:
                    msg = self.name + ' consume '+ queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == "__main__":
    for i in range(500):
        queue.put('initial products ' + str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()


