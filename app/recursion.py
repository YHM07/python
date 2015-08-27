#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def fact(n):
    print '\n==>fact(%d)' %(n) 
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print fact(5)

def fact(n):
    return tail_fact(1,1,n)

def tail_fact(res,cnt,n=1):
    if cnt > n:
        return res
    else:
        return tail_fact(res*cnt,cnt+1,n)

print fact(6)
