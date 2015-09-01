#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import threading
import time

condition = threading.Condition()
products  = 0

class Producer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition
        global products

        while True:
            if condition.acquire():
                if products < 10:
                    products += 1
                    print('Producer {0} deliver one, now products is {1}'.format(self.name, products))
                    condition.notify()
                else:
                    print('Producer {0}: already 10, stop deliver, now products is {1}'.format(self.name, products))
                    condition.wait()
                condition.release()
                time.sleep(2)

class Consumer(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition
        global products

        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print('Consumer {0}: consume one, now products is {1}'.format(self.name, products))
                    condition.notify()
                else:
                    print('Consumer {0}: only one, stop consume,products is {1}'.format(self.name, products))
                    condition.wait()

                condition.release()
                time.sleep(2)

if __name__ == '__main__':
    for p in range(2):
        p = Producer()
        p.start()

    for c in range(10):
        c = Consumer()
        c.start()
