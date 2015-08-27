#!/usr/bin/env python

import os
def cdWalker(cdrom,cdcfile):
    export = ""
    for root,dirs,files in os.walk(cdrom):
        export += "\n %s %s %s" %(root,dirs,files)
    open(cdcfile,'w').write(export)
cdWalker('/home/ubuntu/test/','cd1.cdc')
