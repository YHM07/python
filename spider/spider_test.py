#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import urllib
import urllib.request

# data = {}
# data['word'] = 'Jecvay Notes'

# url_values = urllib.parse.urlencode(data)

# url  = 'http://www.baidu.com/?s'
# full_url = url + url_values

full_url  = 'http://baidu.com'
page = urllib.request.urlopen(full_url)
html = page.read()
html = html.decode('utf-8')
print(html)
