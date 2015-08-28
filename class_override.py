#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class override():
    def __init__(self):
        print('call __init__')
        self.attr = 1
    
    def __new__(self):
        print("call __new__")

    def __del__(self):
        print('call __del__')

    def __str__(self):
        print("call __str__")
        return 'class override str'

    def __repr__(self):
        print('call __repr__')
        return 'class override repr'

    def __unicode__(self):
        print("call __unicode__")
        return 'class override unicode'

    def __nozero__(self):
        print('call __nozero__')
        return 1

    def __len__(self):
        print('call __len__')
        return 1

# callable(instance) True
    def __call__(self):
        print('call __call__')

oa = override()
print(oa)
print(repr(oa))
# unicode(oa)
# print(bool(oa))
# print(len(oa))
# print(callable(oa))

class A(object):
    def __init__(self):
        print('call __init__')
        self.value = 1

    def __new__(cls):
        print('call __new__')
        return super(A,cls).__new__(cls)

a = A()
print(a.value)
