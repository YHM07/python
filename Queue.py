#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import random, threading, time
from queue import Queue 

# producer thread 
class Producer(threading.Thread):

    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self._queue = queue

    def run(self):
        for index in range(10):
            randomnum = random.randint(1,99)
            print('{0}:{1} is producing {2} to the queue'.format(
                time.ctime(), self.name, randomnum))
            self._queue.put(randomnum)
            time.sleep(1)
        print('{0}:{1} finished'.format(time.ctime(), self.getName()))

# Consumer thread 
class Consumer_even(threading.Thread):

    def __init__(self,t_name,queue):
        threading.Thread.__init__(self, name=t_name)
        self._queue = queue

    def run(self):
        while True:
            try:
                val_even = self._queue.get(True, timeout=5)
                if val_even % 2 == 0:
                    print('{0}:{1} is consuming. {2} in the queue is consumed.'.format(time.ctime(), self.getName(), val_even))
                    time.sleep(2)
                else:
                    self._queue.put(val_even)
                    time.sleep(2)
            except:
                print('{0}:{1} finished'.format(time.ctime(), self.getName()))
                break

class Consumer_odd(threading.Thread):

    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self._queue = queue

    def run(self):
        while True:
            try:
                val_odd = self._queue.get(True, timeout=5)
                if val_odd % 2 != 0:
                    print('{0}:{1} is consuming. {2} in the queue is consumed.'.format(time.ctime(), self.getName(), val_odd))
                    time.sleep(2)

                else:
                    self._queue.put(val_odd)
                    time.sleep(2)

            except:
                print('{0}:{1} finished'.format(time.ctime(), self.getName()))
                break

# main thread 

def main():
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer_even = Consumer_even('Con_even', queue)
    consumer_odd  = Consumer_odd('Con_odd', queue)

    producer.start()
    consumer_even.start()
    consumer_odd.start()

    producer.join()
    consumer_even.join()
    consumer_odd.join()

    print('all threads terminate')

if __name__ == '__main__':
    main()

