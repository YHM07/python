#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import threading

count = 0
mutexA = threading.RLock()
mutexB = threading.RLock()
mutex  = threading.RLock()

class myThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # self.setName('new ' + self.name)

    def run(self):
        global count
        global mutex
        if mutex.acquire():
            count += 1
            print('I am {0},set count:{1}'.format(self.name, count))
            if mutex.acquire():
                count += 1
                print('I am {0},set count:{1}'.format(self.name, count))
                mutex.release()
            mutex.release()
#        mutex.acquire()
#        try:
#            count += 1
#        finally:
#            mutex.release()
        self.fun1()
        self.fun2()

    def fun1(self):
        global mutexA, mutexB
        if mutexA.acquire():
            print('I am {0},get res: {1}'.format(self.name, 'ResA'))

            if mutexB.acquire():
                print('I am {0},get res: {1}'.format(self.name, 'ResB'))
                mutexB.release()
        mutexA.release()

    def fun2(self):
        global mutexA, mutexB
        if mutexB.acquire():
            print('I am {0},get res: {1}'.format(self.name, 'ResB'))
            
            if mutexA.acquire():
                print('I am {0},get res: {1}'.format(self.name, 'ResA'))
                mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for thread in range(0,100):
        t = myThread()
        t.start()
    print(count)
