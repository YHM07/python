#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import threading
import time

class MyThread(threading.Thread):

    def __init__(self, signal):
        threading.Thread.__init__(self)
        self._signal = signal

    def run(self):
        print('I an {0}, I will sleep...'.format(self.name))
        self._signal.wait()
        print('I am {0}, I awake...'.format(self.name))

if __name__ == '__main__':
    signal = threading.Event()
    for t in range(3):
        thread = MyThread(signal)
        thread.start()

    print('main thread sleep 3 seconds')
    time.sleep(3)

    signal.set()
