#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import redis
from conf import settings

class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(
                host = settings.RedisServer, 
                port = settings.RedisPort)

        self.chan_sub = settings.RedisSubChannel
        self.chan_pub = settings.RedisPubChannel

    def get(self, key):
        return self.__conn.get(key)

    def set(self, key, values):
        self.__conn.set(key, values)

    def keys(self, pattern = '*'):
        return self.__conn.keys(pattern)

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

if __name__ == '__main__':
    r = RedisHelper()
    r.public('Hello World')
