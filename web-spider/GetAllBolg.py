#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib
import time
import os

CountOfOnePage = 50
CountOfPage    = 7
# url = ['']*CountOfOnePage*CountOfPage

url = [['']*CountOfOnePage for i in range(CountOfPage)]

page = 1
link = 1
index = 0
while page <= CountOfPage:
    src = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_' + str(page)+ '.html').read()
    title = src.find(r'<a title')
    href  = src.find(r'href', title)
    html  = src.find(r'.html', href)
    index = 0
    while index < CountOfOnePage and title != -1 and href != -1 and html != -1:
        url[page][index] = src[href+len(r'href="'):html+len(r'.html')]
        print('{0}: {1}'.format(link, url[page-1][index]))
        title = src.find(r'<a title', html)
        href  = src.find(r'href', title)
        html  = src.find(r'.html', href)
        index += 1
        link  += 1
    else:
        print('page {0} find end'.format(page))
    page += 1
else:
    print('all article find end')

    
