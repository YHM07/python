#!/usr/bin/env python
# -*-coding:utf-8 -*-
import functools
def log(func):
    def wrapper(*args,**kw):
        print 'call %s():' %func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now():
    print '2014/10/16'
    return 'YHM07'

# now = log(now)
print now()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():' %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2014/10/16'
    return 'YHM07'
#now = log('execute')(now)
print now()
print now.__name__
