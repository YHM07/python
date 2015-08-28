#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'H.M.Yang'

import sys

def hello():
    """TODO: Docstring for hello.
    :returns: TODO

    """
    args = sys.argv
    if len(args) == 1:
        print('Hello,world')
    elif len(args) == 2:
        print('Hello,{0}'.format(args[1]))
    else:
        print('Too many arguments')

if __name__ == '__main__':
    hello()
