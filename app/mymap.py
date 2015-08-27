#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mymap(fun,l):
    return [fun(x) for x in l]

print mymap(lambda x:x*x,range(10))

def prod(l):
    return reduce(lambda x,y:x*y,l)

print prod(range(1,6))

