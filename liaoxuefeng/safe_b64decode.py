#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import base64

def safe_b64decode(code):
    m = len(code) % 4
    if m > 0:
#        print base64.b64decode(code)
        code += '='* (4 - m)
    return base64.b64decode(code)

if __name__ == '__main__':
    print safe_b64decode('YWJjZA')
    print safe_b64decode('YWJjZA==')
