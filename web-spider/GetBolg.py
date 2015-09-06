#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'


import urllib
import os
import time

# src = '<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录'

src = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
# print(index)

# src = content

loop = 50
html = 0
url  = ['']*loop
i = 0
while i < loop :
    title = src.find(r'<a title', html)
#    print(title)
#
    href = src.find(r'href=', title)
#    print(href)
#
    html = src.find(r'.html', href)
#    print(html)

    url[i]  = src[href+6:html+5]
    print(url[i])

    i += 1
else:
    print('find end!')

# print(url)

#
#content = urllib.urlopen(url).read()
## print(content)
#
#filename = os.path.split(url)[1]
#with open(filename, 'w') as f:
#    f.write(content)

j = 0
while j < loop:
    content = urllib.urlopen(url[j]).read()
    filename = os.path.split(url[j])[1]
    open(r'hanhan/'+filename, 'w+').write(content)
    j += 1
    time.sleep(15)
else:
    print('write end')
