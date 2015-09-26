#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

def singleton(cls):
    instances = {}

    def wrapper(*args, **kws):
        if cls not in instances:
            instances[cls] = cls(*args, **kws)
        return instances[cls]
    return wrapper


@singleton
class myClass(object):
    def __init__(self, n):
        self.n = n
        print('n --> {0}'.format(n))
        self.tasks = []

c1 = myClass(10)
c1.tasks.append('c1')
c2 = myClass(20)
c2.tasks.append('c2')
print('tasks: {0}'.format(c1.tasks))


class TestAttr(object):
    
    def sayhi(self):
        print('Hello World!')

    def info(self):
        print('I am Alex')

def run():
    print('running outside the class')
    
m = TestAttr()

attr = 'test'

if not hasattr(m, attr):
    setattr(m, attr, run)

func = getattr(m, attr)
func()


