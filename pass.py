#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import hashlib

db = {}
Salt = 'the-Salt'

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

def register(username,password):
    db[username] = get_md5(username + password + Salt)
    print 'register:%s' %  db[username]

def login(username,password):
    md5 = get_md5(username + password + Salt) 
    print 'log:%s' %md5 
#    if db.has_key(username):
    if db[username] == md5:
        print 'True'
    else:
        print 'False'

if __name__ == '__main__':
    register('abc','123456')
    register('mike','88888888')
    register('yhm','password')
    login('abc','123456')

