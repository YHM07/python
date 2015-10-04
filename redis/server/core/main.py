#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import redishelper
import serialize
from conf import hosts 
import time, json, threading


class MonitorServer(object):
    def __init__(self):
        self.r = redishelper.RedisHelper()
#        self.r.set('name', 'alex')
        self.save_config()
#        print(self.r.get('name'))

    def start(self):
        while True:
            self.handle()
            self.data_handle()

    def save_config(self):
        serialize.push_all_configs_into_redis(
                self, 
                hosts.monitored_groups)

    def handle(self):
        chan_sub = self.r.subscribe()
#        while True:
        print('-------- going to parse_response .......\n')
#            print(chan_sub.parse_response())
        host_service_data = chan_sub.parse_response()
        host_service_data = json.loads(host_service_data[2])

        host_service_data['timestamp'] = time.time()

        service_data_key = 'ServiceData::%s::%s' %(
                host_service_data['host'],
                host_service_data['service'])
        self.r.set(service_data_key, json.dumps(host_service_data))


    def data_handle_run(self):
        serialize.data_process(self)

    def data_handle(self):
        '''
        处理监控数据，独立线程
        '''
        t = threading.Thread(
                target = self.data_handle_run)
        t.start()

    def alert_handle(self):
        '''
        处理报警信息，独立线程
        '''
        pass


