# _*_ coding: utf-8 _*_
import os
ifile = open('test.txt','r')
ofile = open('result.txt','w')
num = 1
for line in ifile.readlines():
    print line
    print num
    num = num + 1
    if ((line.startswith('#') != 1) and (line != '\n')):
        ofile.write(line)
#    if (line != '\n')
# for line in ifile.readline():
#    if line.startswith('#'):
#        ofile.write(line)
ifile.close()
ofile.close()
