#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import logging
logging.basicConfig(level=logging.INFO)
import pdb
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as err:
    print('except:',err)
finally:
    print('finally...')
print('END')
pdb.set_trace()

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s)
#def main():
#    try:
#        bar(0)
#    except Exception as err:
#        print('except:',err)
#    finally:
#        print('finally...')

#def main():
#    try:
#        bar('0')
#    except Exception as err:
#        logging.exception(err)

# main()
print('END')

def foo(s):
    n = int(s)
#    if n == 0:
#        raise ValueError('invalid value: %s'% s)
    # assert n != 0, 'n is zero!'
    logging.info('n = {0}'.format(n))
    return 10 / n

def bar():
#    try:
        foo('0')
#    except ValueError as e:
#        print('ValueError')
#        raise
#
bar()
