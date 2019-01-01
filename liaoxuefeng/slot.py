#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''to test slot'''

__author__='H.M.Yang'

from types import MethodType
class Student(object):
#    #__slots__=('name','age') # 用tuple定义允许绑定的属性名称
#    def get_score(self):
#        return self.score
#    def set_score(self,score):
#        if not isinstance(score,int):
#            raise ValueError('score must be an integer')
#        if score < 0 or score > 100:
#            raise ValueError('score must between 0 ~ 100')
#        self.score = score
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = score
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,birth):
        self._birth = birth
    @property
    def age(self):
        return 2014 - self._birth
s = Student()
# s.name = 'YHM'
# s.age  = 'man'
# s.score= 90
# setattr(Student,'score',90)
# print s.score
# Student.score = MethodType(score,None,Student)
# s.set_score(90)
# print s.get_score()
# s.set_score(900)
# 
# class GraduateStudent(Student):
#     __slots__=('name','age')
#     def __init__(self,name=''):
#         self.name = name
# 
# g = GraduateStudent()
# g.score = 90
# g.power = 'huk'

s.score = 989
print s.score
s.birth = 1989
print s.birth
print s.age
