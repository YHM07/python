#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def fun(a,b,c=0,*args,**kw):
    print 'a=',a,'\tb=',b,'\tc=',c,'\targs=',args,'\tkw=',kw

print '\n==>fun(1,2)'
fun(1,2)
print '\n==>fun(1,2,3)'
fun(1,2,3)
print '\n==>fun(1,2,3,4)'
fun(1,2,3,4)
print '\n==>fun(1,2,3,4,5)'
fun(1,2,3,4,5)
print '\n==>fun(1,2,3,4,5,k1=6,k2=7)'
fun(1,2,3,4,5,k1=6,k2=7)
#print '\n==>fun(1,2,c=3,4,5,k1=6,k2=7)'
#fun(1,2,c=3,4,5,k1=6,k2=7)
print '\n==>fun(1,2,k1=6,k2=7)'
fun(1,2,k1=6,k2=7)
print '\n==>fun(*(1,2))'
fun(*(1,2))
print '\n==>fun(*(1,2,3))'
fun(*(1,2,3))
print '\n==>fun(*(1,2,3,4))'
fun(*(1,2,3,4))
print '\n==>fun(*(1,2,3,4,5))'
fun(*(1,2,3,4,5))
print '\n==>fun(*(1,2,3,4,5),**{\'k1\':8,\'k2\':9})'
fun(*(1,2,3,4,5),**{'k1':8,'k2':9})
print '\n==>fun(*(1,2,3,\'4\',\'a\'),**{\'k1\':8,\'k2\':9})'
fun(*(1,2,3,'4','a'),**{'k1':8,'k2':9})

print '\n==>fun(*(1,))'
fun(*(1,))



