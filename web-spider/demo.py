#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib
import urllib2

# response = urllib2.urlopen('http://www.baidu.com')
# print(response.read())

# request = urllib2.Request('http://www.baidu.com')
# response = urllib2.urlopen(request)
# html = response.read()
# print(html)

values = {}
values['username'] = 'qzfengshang@sina.com'
values['password'] = '199019370707'

data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# geturl = url + '?' + data
# print(geturl)

# request = urllib2.Request(geturl)
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
html = response.read()
print(html)
