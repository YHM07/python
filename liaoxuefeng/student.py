#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''class student'''

__author__='H.M.Yang'

class student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print '%s:%s' %(self.__name,self.__score)

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        score = float(score)
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def __rename(self,name):
        self.__name = name
    def rename(self,name):
        self.__rename(name)

if __name__=='__main__':
    bart=student('Bart',59)
    bart.age = '39'
    print bart.age
    lisa=student('Lisa',90)
    bart.print_score()
    lisa.print_score()
    bart.age = 50
    print bart.age
    print bart.get_name()
    print bart.get_score()
