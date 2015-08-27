#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

def log(text='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print 'begin call %s()' % func.__name__
            print '%s %s()' %(text,func.__name__)
            func(*args,**kw)
            print 'end call %s()' % func.__name__
        return wrapper
    return decorator

@log
def foo():
    pass
@log('execute')
def foo():
    pass

foo()
