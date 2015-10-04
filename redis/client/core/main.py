#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import json
import time
import redishelper
import threading

from conf import settings
from plugins import plugin_api

class MonitorClient(object):
    def __init__(self):
        self.r = redishelper.RedisHelper()
        self.ip = settings.ClientIP
        self.host_config = self.get_host_config()

    def start(self):
        self.handle()

    def get_host_config(self):
        config_key = 'HostConfig::%s' %self.ip
        config = self.r.get(config_key)
        if config:
            config = json.loads(config)
        return config

    def handle(self):
        if self.host_config:
            while True:
                for service, val in self.host_config.items():
#                    print(service, val)
                    if len(val) < 3: 
                        self.host_config[service].append(0)
                    # 服务:包括以下三项
                    plugin_name, interval, last_run_time = val

                    if time.time() - last_run_time < interval:
                        next_run_time = interval - (time.time() - last_run_time)
                        print('service \033[31;1m[{0}]\033[0m next run time is in \033[32;1m[{1}]\033[0m secs'.format(service, next_run_time))
                    else:
                        print("\033[32;1mgoing to run the \033[31;1m[{0}]\033[0m again\033[0m".format(service))
                        self.host_config[service][2] = time.time()

                        t = threading.Thread(
                                target = self.call_plugin, 
                                args = (service, plugin_name))
                        t.start()
                time.sleep(1)
        else:
            print("\033[31;1mCannot get host config\033[0m")

    def call_plugin(self, service_name, plugin_name):
        func = getattr(plugin_api, plugin_name)
        service_data = func()

        report_data = {
                'host'   : self.ip,
                'service': service_name,
                'data'   : service_data,
                }
        self.r.public(json.dumps(report_data))

if __name__ == '__main__':
    m = MonitorClient()
    m.start()

