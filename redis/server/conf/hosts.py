#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import templates

web_clusters = templates.LinuxGenericTemplate()
web_clusters.hosts = [
        '192.168.1.112',
#        '192.169.1.105',
        ]
# web_clusters.services = []

mysql_groups = templates.LinuxTemplate()
mysql_groups.hosts = [
        '192.168.1.112',
#        '192.168.1.105',
        ]
# mysql_groups.services = []

monitored_groups = [
        web_clusters,
        mysql_groups
        ]
    
if __name__ == '__main__':
    host_config_dict = {
            
            }
    for group in monitored_groups:
        print(group.name) 
        for h in group.hosts:
            print("\t {0} : {1}".format(h, group.services))
            if h not in host_config_dict:
                host_config_dict[h] = {}
            for s in group.services:
#                host_config_dict[h] = {
#                        s.name : [s.plugin_name, s.interval]
                host_config_dict[h][s.name] = [s.plugin_name, s.interval]
                        
    for h, v in host_config_dict.items():
        print(h, v)

