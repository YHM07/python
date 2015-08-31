#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A():
    def __init__(self, value):
        self.value = value

    def __cmp__(self, obj):
        print 'call __cmp__'
        return self.value - obj.value

    def __lt__(self, obj):
        print 'call __lt__'
        return self.value < obj.value

    def __gt__(self, obj):
        print 'call __gt__'
        return self.value > obj.value

    def __eq__(self, obj):
        print 'call __eq__'
        return self.value == obj.value

a1 = A(1)
a2 = A(2)
print cmp(a1, a2)
print a1 < a2
print a1 > a2
print a1 == a2

