#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

CDROM = '/home/ubuntu/test/'
def cdWalker(cdrom,cdcfile):
    export = ""
    for root,dirs,files in os.walk(cdrom):
        export += "\n %s;%s;%s" %(root,dirs,files)
        open(cdcfile,'w').write(export)
if "-e" == sys.argv[1]:
    if dirs in os.walk(sys.argv[2])
        print dirs
    cdWalker(CDROM,sys.argv[2])
    print "record information  %s" % sys.argv[2]
else:
    print '''cday32 usage:
    python cday32.py -e mycdc.cdc
    # 将光盘信息记录到mycdc.cdc
    '''
