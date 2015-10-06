#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib, urllib2
from bs4 import BeautifulSoup

# page = 1
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# headers = {
#         'Connection': 'Keep-Alive',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# #        'Accept-Encoding': 'gzip,deflate,sdch',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
#         'Accept-Language': 'zh-CN,zh;q=0.8',
#         }
# 
# try:
#     request = urllib2.Request(url, headers = headers)
#     response = urllib2.urlopen(request)
#     html = response.read()
# 
#     soup = BeautifulSoup(html,'lxml')
#     class_attr = "article block untagged mb15"
#     paragraphs = soup.find_all('div', class_=class_attr)
#     for paragraph in paragraphs: 
#         author = paragraph.find('div', class_="author")
#         votes  = paragraph.find('i', class_="number")
#         content = paragraph.find('div', class_="content")
#         if author:
#             print author.get_text().strip(), votes.get_text()
#         print content.get_text().strip()
#         print('\n')
# 
# except urllib2.URLError, e:
#     if hasattr(e, 'code'):
#         print(e.code)
#     if hasattr(e, 'reason'):
#         print(e.reason)


# 糗事百科类
class QSBK(object):
    def __init__(self):
#        self.pageIndex = 1
        self.headers = {
                'Connection': 'Keep-Alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#        'Accept-Encoding': 'gzip,deflate,sdch',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                }
# 存放段子的变量，每一个元素是每一页的段子
#        self.stories = []
# 存放程序是否继续运行的变量
#        self.enable = False

    def getPage(self, url):
        try:
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
#            html = response.read().decode('utf-8')
            html = response.read()
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print('连接糗事百科失败：',e.code)
            if hasattr(e, 'reason'):
                print('连接糗事百科失败：',e.reason)
            html = None
#        finally:
#            pageIndex += 1
        return html

    def getItems(self,html):
#        html = self.getPage(url)
        if not html:
            print('-------Page load error!----')
            return None
        soup = BeautifulSoup(html, 'lxml')
        pageStories = []

        item_attr = "article block untagged mb15"
        items = soup.find_all('div', class_ = item_attr)
        for item in items:
            author = item.find('div', class_='author')
            votes  = item.find('i', class_='number')
            content = item.find('div', class_='content')
            if author:
                story = [
                        author.get_text().strip(),
                        votes.get_text().strip(),
                        content.get_text().strip()
                        ]
                pageStories.append(story)
        return pageStories

    def run(self, url):
        html = self.getPage(url)
        pageStories = self.getItems(html)
        for story in pageStories:
            print 'author: ', story[0], '\tvotes: ', story[1], '\n',\
                    story[2]
if __name__ == '__main__':
    spider = QSBK()
    pageIndex = 1
    while True:
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        spider.run(url)
        input = raw_input()
        if input.lower() == 'q':
            break
        pageIndex += 1
