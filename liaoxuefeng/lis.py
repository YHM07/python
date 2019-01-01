#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A():
    def __init__(self):
        print 'call __init__'
        self.value = [1,2,3,4,5];

    def __len__(self):
        print 'call __len__'
        return len(self.value)

    def __getitem__(self, index):
        print 'call __getitem__'
        return self.value[index]
    
    def __setitem__(self, index, value):
        print 'call __setitem__'
        self.value[index] = value

    def __delitem__(self, index):
        print 'call __delitem__'
        del self.value[index]

a = A()
print len(a)
print a[2]
a[2] = 99
del a[2]
print a

