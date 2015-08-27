#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import getopt

CDROM = '/home/ubuntu/test/'
def cdWalker(cdrom,cdcfile):
    export = ""
    for root,dirs,files in os.walk(cdrom):
        export += "\n %s;%s;%s" % (root,dirs,files)
        open(cdcfile,'w').write(export)
def usage():
    print ("usage:%s [-e|-d][--help|--output] args..." % sys.argv[0])
if "__main__" == __name__:
    try:
        opts,args = getopt.getopt(sys.argv[1:],"e:d:")
        print ("="*10,"opts","="*10)
        print (opts)
        # check all param
        for opt,arg in opts:
            if opt in ("-h","--help"):
                usage()
                sys.exit(1)
            elif opt in ("-e"):
                cdWalker(CDROM,arg)
            else:
                pass
    except getopt.GetoptError:
        print "Getopt error"
        usage()
        sys.exit(1)
        
