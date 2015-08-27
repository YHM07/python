#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# name = raw_input("Input you name:")
# print "Hello,",name
import math
print r'''line1
    line2 \\\\\\
    line3'''
print u'中文'
age = int(raw_input('Please enter you age: '))
if age < 2000:
    print '00前'
else:
    print '00后'
d = {'Michael':95,'Bob':75,'Tracy':85}
def mabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
print mabs(129)
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x,y = move(100,100,60,math.pi / 6)
print x,y
x = move(100,100,60,math.pi / 6)
print x

def powr(x,n=2):
    res = 1
    while n > 0:
        res = res * x
        n = n -1
    return res
print powr(5)
print powr(5,3)

def add_end(L=[]):
    L.append('END')
    return L
print add_end()
print add_end([1,2,3])
print add_end()
print add_end()
print add_end([1,2,3])
print add_end([1,2,3])

def calc(*nums):
    s = 0
    for n in nums:
        s = s + n * n
    return s
print calc(1,2,3)
print calc()
nums = [1,2,3]
print calc(*nums)
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw
person('Michael',30)

person('Bob',35,city='BeiJing')
person('Admn',45,gender='M',job='Engineer')
kw = {'city':'BeiJing','job':'Engineer'}
person('Jack',40,**kw)
