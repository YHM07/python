#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

from multiprocessing import Process, Pipe, Queue

def run(conn, q):
    conn.send([42, None, 'Hello World'])
    conn.send('test')
    q.put('hahhah')
    conn.close()

if __name__ == '__main__':
    A, B = Pipe()
    Q = Queue()

    p = Process(target=run, args=(B, Q))
    p.start()
    print(A.recv())
    print(A.recv())

    print('from q: %s'% Q.get())
    p.join()

