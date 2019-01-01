#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' raise except '''

__author__='H.M.Yang'

import logging
import pdb
logging.basicConfig(level=logging.INFO)
# try:
#     print 'try...'
#     r = 10/int(5)
#     print 'result:',r
# except ValueError,e:
#     print 'ValueError ',e
# except ZeroDivisionError,e:
#     print 'except:',e
# else:
#     print 'No error'
# finally:
#     print 'finally...'
# print 'END'

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    # if n == 0:
    pdb.set_trace() 
    #     raise FooError('Invalid value:%s' %s) 
    # assert n!=0,'n is zero'
    logging.info('n=%d' % n)
    return 10/n
def  bar(s):
    return foo(s)*2
def main():
    #try:
        bar('0')
    #except StandardError,e:
    #    logging.exception(e)
        print 'Error!'
    #    raise
    #finally:
        print 'finally'

if __name__=='__main__':
    main()
