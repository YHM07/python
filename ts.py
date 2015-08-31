#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello',name)
def myabs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

myabs(2)

def quadratic(a,b,c):
    if not isinstance((a,b,c),(int, float)):
#        raise TypeError('bad operand type (int or float)')
        pass
    d = b*b - 4*a*c
    if d < 0:
        print('no solution')
        return
    else:
        r1 = (-b+math.sqrt(d))/2/a
        r2 = (-b-math.sqrt(d))/2/a 
        return r1,r2 

r = quadratic(2,3,1)
print(r)

def fun1(a,b,c=0,*args,**kw):
    print('a =',a, 'b =', b, 'c =',c, 'args = ', args, 'kw = ', kw)

#fun1(1,2,3,'a','b',**{'x':9})
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
fun1(*args, **kw)

def move(n,a,b,c):
    if n == 1:
        print('move',a, '-->', c)
        return
    move(n-1,a,c,b)
    print('move',a, '-->', c)
    move(n-1,b,a,c)

move(3,'A','B','C')

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

def fact(n):
    if n == 1:
        return 1
    else:
        return fact_iter(n,1)
def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num-1, num*product)

print(fact(5))

def triangles():
    L = [1]
    n = 1
    yield L
    while True:
        a = [0] + L
        b = L + [0]
        n = n + 1
        L = [a[i] + b[i] for i in range(0,n)]
        yield L
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

from functools import reduce
def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

r = reduce(fn,map(char2num, '13579'))
print(r)

def normalize(name):
    u = name[0].upper()
    o = name[1:].lower()
    return u + o
L1 = ['adam','LISA','bar']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce 
def prod(L):
    def multi(x,y):
        return x*y
    return reduce(multi, L)

print('3*5*7*9=', prod([3,5,7,9]))

from functools import reduce
def str2float(s):
    l = s.split('.')
    f1 = reduce(lambda x,y: x*10+y, map(char2num,l[0]))
    f2 = reduce(lambda x,y: x*10+y, map(char2num,l[1]))
    return f1+0.1**len(str(f2))*f2

print('str2float(\'123.456\') = ', str2float('123.456'))

sentences = ['Mary read a story to Sam and Isla.',
        'Isla cuddled Sam.',
        'Sam chortled.']
print(reduce(lambda a, x:a+x.count('Sam'),sentences,0))

def str2float(s):
    l,r = s.split('.')
    f1  = reduce(lambda x,y: x*10+y,map(int, l))
    f2  = reduce(lambda x,y:x/10+y, map(int,r[::-1]))/10
    return f1 + f2
print('str2float(\'123.456\') = ', str2float('123.456'))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
#        print(n)
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
#    print(it)
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
#        print(it)

for n in primes():
    if n < 10:
        print(n)
        pass
    else:
        break

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
# output = filter(is_palindrome, range(1,1000))
# print(list(output))
# 
# output = filter(lambda x: str(x) == str(x)[::-1], range(1,1000))
# print(list(output))

ir = sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
print(ir)

L = [('Bob',75), ('Adam',92), ('Bart',66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L, key=lambda x:x[1], reverse=True)
print(L3)

def pow_three():
    fs = []
    for i in range(1,4):
        def f(i = i):
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = pow_three()
print(f1(), f2(), f3())
