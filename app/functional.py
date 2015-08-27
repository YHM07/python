#!/usr/bin/env python
# -*-coding:utf-8 -*-

def fun(x,y):
    return x*10 + y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print reduce(fun,map(char2num,'13579'))
print isinstance(reduce(fun,map(char2num,'13579')),int)

def str2int(s):
    return reduce(fun,map(char2num,s))

print str2int('13579')

def descend(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([36,5,12,9,21],descend)

def cmp_ignore_case(s1,s2):
    s1 = s1.upper()
    s2 = s2.upper()
    if s1 < s2:
        return 1
    if s1 > s2:
        return -1
    return 0
print sorted(['about', 'bob', 'Zoo', 'Credit'])
print sorted(['about', 'bob', 'Zoo', 'Credit'],cmp_ignore_case)

def lazy_sum(*args):
    def sum():
        res = 0
        for i in args:
            res = res + i
        return res
    return sum

f = lazy_sum(*range(5))
print f()
