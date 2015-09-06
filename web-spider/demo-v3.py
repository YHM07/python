#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib
import urllib.request

# request = urllib.request.Request('http://www.baidu.com')
# response = urllib.request.urlopen(request)
# html = response.read()
# print(html)

val = {}
val['username'] = 'qzfengshang@sina.com'
val['password'] = '199019370707'

data = urllib.urlencode(val)
url  = "http://passport.csdn.net/account/login"
geturl = url + '?' + data
print(geturl)
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
html = response.read()
# print(html)


