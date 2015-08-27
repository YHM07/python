#!/usr/bin/env python
# -*- coding:utf-8 -*-

import functools
def factor(a):
    d = 2
    while (d <= (a/2)):
        if ((a/d) * d == a):
            return (a/d,d)
        d = d + 1
    return (a,1)

x,y = factor(5)
print x,y

a = 0
def fc():
    def p():
        global a
        a = a+1
        return a
    return p

def fg():
    a,b = 0,1
    while 1:
        yield b
        a,b = b ,a+b

x = fc()
y = fg()
for i in range(10):
    print(x(),next(y))

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'begin call %s()' %func.__name__
        func(*args,**kw)
        print 'end call %s()' %func.__name__
    return wrapper

@log
def now():
    print '2014/10/17'
#    return 'end call %s()' %now.__name__ 

print now()

def log(text='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print 'begin call %s()' %func.__name__
            print '%s %s()' % (text,func.__name__)
            func(*args,**kw)
            print 'end call %s()' %func.__name__
        return wrapper
    return decorator

@log('Hello')
def now():
    print '2014/10/17'

print 'the second'
now()
