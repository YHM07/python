#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class test
"""

__author__ = 'H.M.Yang'

class student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('{0}:{1}'.format(self.__name, self.__score))

tom = student('tom',80)
jack = student('jack',90)

tom.print_score()
jack.print_score()

jack.age = 18
print('jack age: {0}'.format(jack.age))

class student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if not isinstance(val, int):
            raise ValueError('score must be integer!')
        if val < 0 or val > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = val

    @property
    def age(self):
        return 25

s = student()
s.score = 60
print(s.score)
print(s.age)
# s.score = 999

class screen(object):
    
    def __init__(self):
        print('screen init')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height

s = screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d?' % s.resolution

class A(object):

    def __init__(self):
        print('A.__init__() first')
        self.__private()
        self.public()
        print('A.__init__() second')

    def __private(self):
        print('A.__private()')

    def public(self):
        print('A.public()')

class B(A):
    def __private(self):
        print('B.__private()')

    def public(self):
        print('B.public()')

b = B()

#print('\n'.join(dir(B)))

class chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda username : chain('{0}:{1}'.format(self._path, username))
        else:
            return chain('{0}/{1}'.format(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# print(chain().status.user.timeline.list)
print(chain().github.com.users('michael').repos)



