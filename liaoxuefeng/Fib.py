#!/usr/bin/env python 
# -*- coding: utf-8 -*-

''' __iter__'''

__author__='H.M.Yang'

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 20:
            raise StopIteration();
        return self.a

class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            print start
            stop  = n.stop
            print stop
            a,b = 1,1
            L  = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

