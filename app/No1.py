#!/usr/bin/python 
# _*_ coding:utf-8 _*_

import os
import sys
import getopt

def usage():
    print("Usage:%s [-a|-o|-c|-t] [--help|--output] args..." % sys.argv[0])
if "__main__" == __name__:
    #lsArgs = [""]
    try:
        opts,args = getopt.getopt(sys.argv[1:],"ao:ct:",["help","output=","test"])
        print("=============opts=============")
        print(opts)

        print("=============args=============")
        print(args)

        # check all param
        for opt,arg in opts:
            if opt in ("-h","--help"):
                usage()
                sys.exit(1)
            elif opt in ("-t","--test"):
                print("for test option")
            else:
                print("%s ==> %s" %(opt,arg))
    except getopt.GetoptError:
        print("getopt error!")
        usage()
        sys.exit(1)
