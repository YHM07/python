# _*_ coding: utf-8  _*_
import os
# print os.listdir("/home/ubuntu/test/")
export = []
for root,dirs,files in os.walk('/home/ubuntu/test/'):
    print dirs
    export.append("\n %s;%s;%s" % (root,dirs,files))
open('mycdc.cdc','w').write('' .join(export))
