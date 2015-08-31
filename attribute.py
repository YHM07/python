#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A():
    def __init__(self):
        self.value = 1

    def __getattr__(self, attr):
        print 'call __getattr__'
        try:
            return self.__dict__[attr]
        except:
            return 'not found'

    def __setattr__(self, attr, value):
        print 'call __setattr__'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print 'call __delattr__'
        del self.__dict__[attr]

    def __getattribute__(self, attr):
        print 'call __getattribute__'
        return self.__dict__[attr]

    def __get__(self, attr):
        pass

    def __set__(self, attr, value):
        pass

    def __del__(self):
        pass

a = A()
print getattr(a, 'value')
print getattr(a, 'name')
del a.value

