#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib2
from bs4 import BeautifulSoup
import re

class BDTB(object):
    def __init__(self, baseURL, seeLZ=1, floorTag=1):
        self.headers = {}
        self.baseURL = baseURL
        # 是否只看楼主
        self.seeLZ = '?see_lz=' + str(seeLZ)
        # 楼层编号，初始为1
        self.floor = 1 
        # 默认标题
        self.defaultTitle = u'百度贴吧'

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            html = response.read()
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print('连接百度贴吧失败：', e.code)
            if hasattr(e, 'reason'):
                print('连接百度贴吧失败：', e.reason)
            html = None
        return html

    def getTitle(self, soup):
        return soup.title.get_text()

    def getPageNum(self, soup):
        l_reply = soup.find('li', class_='l_reply_num')
        num = l_reply.find_all('span', class_="red")[1].get_text()
        return num

    def getContent(self, html):
#        soup = BeautifulSoup(html, 'lxml')
        contents = []
        stories = soup.find_all('div', id = re.compile(r"post_content_\d{11}"))
        for story in stories:
            contents.append(story.get_text())
        return contents

if __name__ == '__main__':
#    baseURL = 'http://tieba.baidu.com/p/3138733512'
    baseURL = 'http://tieba.baidu.com/p/'
    print(u"请输入帖子代号：")
    code = raw_input('http://tieba.baidu.com/p/')
    baseURL = baseURL + code
    seeLZ = raw_input('是否只获取楼主发言(1/0)')
    floorTag = int(raw_input('是否写入楼层信息(1/0)'))

    spider = BDTB(baseURL, seeLZ, floorTag)
    pageNum = 1

    html = spider.getPage(pageNum)
    soup = BeautifulSoup(html, 'lxml')

    title = spider.getTitle(soup)
    if not title:
        title = spider.defaultTitle
    print title

    pageNums = spider.getPageNum(soup)
    print u'共', pageNums, u'页'

    for pageNum in range(2, int(pageNums)+1):
        html = spider.getPage(pageNum)
        soup = BeautifulSoup(html, 'lxml')
        contents = spider.getContent(html)
        for story in contents:
            print floorTag, u'楼-----------------------------------------'
            print story
            floorTag += 1


    
        






