#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

from bs4 import BeautifulSoup
import urllib2

def get_menu(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    chapterlist = soup.find_all('ul', class_='chapterlist')
    menu = []
    chapterlist = chapterlist[1]
    chapterlist = chapterlist.find_all('li')
    for chaper in chapterlist:
        addr  = chaper.a['href']        # 各章节地址
        title = chaper.a.contents[0]    # 个章节标题
        menu.append([addr, title])
    return menu 

def get_content(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find_all('div',id='content')
    content = content[0].text.encode('utf-8')
    return content

    
if __name__ == "__main__":
    url = "http://www.tywx.com/ty102148/"
    menu = get_menu(url)
    for chapter in menu[1357:]:
        addr = chapter[0]
        title = chapter[1]
        chapter_url = url + addr.split('/')[2]
        content = get_content(chapter_url)
        with open('novel.txt','a') as f:
            f.write(title.encode('utf-8'))
            f.write('\n')
            f.write(content)
            f.write('\n')

