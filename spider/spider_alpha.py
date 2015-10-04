#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import re
import urllib.request
import urllib.parse

from collections import deque

queue = deque()
visited = set()

url = 'http://iplayboy.tk/'
# url = 'http://news.dbanotes.net'

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url} # 标记为已经访问过

    print('已经获取: ' + str(cnt) + ' 正在抓取 <---' + url )

    cnt += 1
    webpage = urllib.request.urlopen(url)
    if 'html' not in webpage.getheader('Content-Type'):
        continue

# 避免程序异常终止， 用try--catch处理异常
    try:
        html_content = webpage.read().decode('utf-8')
        print(html_content)
#         fd = open('iplayboy.html','wb')
#         fd.write(html_content)
#         fd.close()
        with open('iplayboy.html', 'w') as f:
            f.write(html_content)

    except:
        continue

# 正则表达式提取页面中所有队列，并判断是否访问过，然后加入待爬队列
    linkre = re.compile("href='(.+?)'")
    for x in linkre.findall(html_content):
        queue.append(x)
        print('加入队列 --->' + x)

