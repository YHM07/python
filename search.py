#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' search some directory and files '''

__author__ = 'H.M.Yang'

import os
import sys

def search(path,ext):
    for x in os.listdir(path):
    #    print x
        if os.path.isfile(os.path.join(path,x)):
            if os.path.splitext(os.path.join(path,x))[1] == ext:
                # print os.path.join(os.path.abspath(path),x)
                print os.path.join(path,x)
        if os.path.isdir(os.path.join(path,x)):
            #print os.path.abspath(x)
            #print os.path.join(path,x)
            search(os.path.join(path,x),ext)
            # search(x)

if __name__ == '__main__':
    path = sys.argv[1]
    ext  = sys.argv[2]
    search(path,ext)

