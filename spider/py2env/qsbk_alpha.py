#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib, urllib2
import re
from bs4 import BeautifulSoup

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#        'Accept-Encoding': 'gzip,deflate,sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        }
# try:
#     request = urllib2.Request(url, headers = headers)
#     response = urllib2.urlopen(request)
#     print(response.read())
# except urllib2.URLError, e:
#     if hasattr(e, 'code'):
#         print(e.code)
#     if hasattr(e, 'reason'):
#         print(e.reason)

# try:
#     request = urllib2.Request(url,headers = headers)
#     response = urllib2.urlopen(request)
#     content = response.read().decode('utf-8')
#     pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
#             '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
#     items = re.findall(pattern,content)
#     for item in items:
#         haveImg = re.search("img",item[3])
#         if not haveImg:
#             print item[0],item[1],item[2],item[4]
# except urllib2.URLError, e:
#     if hasattr(e,"code"):
#         print e.code
#     if hasattr(e,"reason"):
#         print e.reason

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
#    with open('baike.html', 'w') as f:
#        f.write(html)

    soup = BeautifulSoup(html,'lxml')
    class_attr = "article block untagged mb15"
    paragraphs = soup.find_all('div', class_=class_attr)
    for paragraph in paragraphs: 
        author = paragraph.find('div', class_="author")
        votes  = paragraph.find('i', class_="number")
        content = paragraph.find('div', class_="content")
        if author:
            print author.get_text().strip(), votes.get_text()
        print content.get_text().strip()
        print('\n')

except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)

