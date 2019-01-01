#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

"""
with...as..
上下文管理器
任何自定义了__enter__ 和 __exit__方法的对象都可以用于上下文管理器
"""

class VOW(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = 'I say: ' + self.text
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + "!"

with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)


