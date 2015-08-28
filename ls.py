#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
            # os.chdir(f)
            # y = os.path.join(path,f)
            # getfile('.',ext)
            getfile(os.path.join(pwd,f),ext)
            # os.chdir(pwd)
        if os.path.isfile(os.path.join(pwd,f)) and os.path.splitext(os.path.join(pwd,f))[1] == ext:
                print(os.path.join(path, f))
                
getfile('.','.py')

