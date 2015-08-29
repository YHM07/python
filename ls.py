#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
"""
__author__ = 'H.M.Yang'

import os
import pdb

def ls(*args):
    f = os.listdir('.')
    for x in f:
        print(x)

# ls()

def getfile(path, ext):
    # pwd = os.path.abspath(path)
    pwd = path
    for f in os.listdir(pwd):
        if os.path.isdir(os.path.join(pwd,f)):
            # pdb.set_trace()
            os.chdir(f)
            # y = os.path.join(path,f)
            getfile(os.path.join(os.path.pardir,f),ext)
            # getfile(os.path.join(pwd,f),ext)
            os.chdir(os.path.pardir)
        if os.path.isfile(os.path.join(pwd,f)) and os.path.splitext(os.path.join(pwd,f))[1] == ext:
                print(os.path.join(path, f))
                
getfile('.','.py')

