#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib2
import cookielib

# # 声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)

# # load cookie file
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar()
# # 从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard = True, ignore_expires = True)

# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 此处的opener方法同urllib2.urlopen()方法，可以传入request
url = 'http://www.baidu.com'
response = opener.open(url)

# 保存cookie到文件
cookie.save(ignore_discard = True, ignore_expires = True)

for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

