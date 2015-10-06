#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import os, sys
from core import main

# base_dir = os.path.dirname(os.path.dirname(__file__))
# #print(base_dir)
# sys.path.append(base_dir)


if __name__ == '__main__':
    server = main.MonitorServer()
    server.start()
