#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib.parse
import urllib.request
import re, os
from   collections import deque
import http.cookiejar

Q = deque()
visited = set()

header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#        'Accept-Encoding': 'gzip,deflate,sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        }

# url = 'http://iplayboy.tk'
url = 'http://www.baidu.com'
Q.append(url)

while Q:
    url = Q.popleft()
    visited |= {url}
    req = urllib.request.Request(url, headers = header)

    try:
        html = urllib.request.urlopen(req)
#        if 'html' not in html.getheader('Content-Type'):
#            continue
    except:
        continue 

    html_content = html.read().decode('utf-8')
 #   print(html_content)
    filename = os.path.split(url)[1]
    with open(r'web/'+filename, 'w+') as f:
        f.write(html_content)


# 正则表达式提取页面中所有队列，并判断是否访问过，然后加入待爬队列
    linkre = re.compile("href='(.+?)'")
    for x in linkre.findall(html_content):
        queue.append(x)
        print('加入队列 --->' + x)

def makeMyopener(head = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#        'Accept-Encoding': 'gzip,deflate,sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, val in head.items():
        elem = (key, val)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makeMyopener()
uop  = oper.open(url, timeout = 1000)
data = uop.read().decode('utf-8')
with open(r'web/'+'test.html', 'w+') as f:
    f.write(data)

