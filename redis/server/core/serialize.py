#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

from conf import hosts
import json, time, operator


def push_all_configs_into_redis(main_ins, monitored_groups):
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
        host_config_key = 'HostConfig::%s' %h
        main_ins.r.set(host_config_key, json.dumps(v))

def fetch_all_config(host_groups):
    host_config_dict = {}
    for group in host_groups:
        for h in group.hosts:
            print("\t {0} : {1}".format(h, group.services))
            if h not in host_config_dict:
                host_config_dict[h] = {}
            for s in group.services:
                host_config_dict[h][s.name] = s                       
    for h, v in host_config_dict.items():
        host_config_key = 'HostConfig::%s' %h
        print("\033[31;1mHost [{0}] Service [{1}]\033[0m".format(h, v))
#        main_ins.r.set(host_config_key, json.dumps(v))
    return host_config_dict 

def data_process(main_ins):
    print("----going to handle monitor data ------")
    all_host_configs = fetch_all_config(hosts.monitored_groups)

    for ip, service_dic in all_host_configs.items():
        for service_name, s_instance in service_dic.items():
            service_redis_key = 'ServiceData::%s::%s' %(
                    ip,
                    service_name)
            s_data = main_ins.r.get(service_redis_key)
            if s_data:
                s_data = json.loads(s_data)
#                print("### > {0}".format(s_data))

                timestamp = s_data['timestamp']
                if time.time() - timestamp < s_instance.interval:
                    if s_data['data']['status'] == 0: # data valid
                       print("\033[32;1mHost [{0}] Service [{1}] valid\033[0m".format(ip, service_name)) 
                       for item_key, val_dic in s_instance.triggers.items():
                           service_item_handle(main_ins, item_key, val_dic, s_data)
                    else:
                        print("\033[31;1mHost [{0}] Service [{1}] pluin error\033[0m".format(ip, service_name))
                else: # data expired
                    expired_time = time.time() - timestamp - s_instance.interval
                    print("\033[31;1mHost [{1}] service [{0}] data expired {2} secs\033[0m".format(ip, service_name, expired_time))

            else:
                print("\033[31;1mNo data found in redis for service [{0}] host [{1}]\033[0m".format(service_name, ip))
    
def service_item_handle(main_ins, item_key, val_dic, client_service_data):
    print("\033[31;1m-----------------Service-item-handle--------------\033[0m")
    print(item_key, client_service_data['data'][item_key])
    
    item_data = client_service_data['data'][item_key]
    warning_val = val_dic['warning']
    critical_val = val_dic['critical']
    oper = val_dic['operator']
    oper_func = getattr(operator, oper)

    if val_dic['data_type'] is float:
        item_data = float(item_data)
        warning_res = oper_func(item_data, warning_val)
        critical_res = oper_func(item_data, critical_val)
        print('warning: [%s], critical: [%s]' % (warning_val, critical_val))
        print('warning: %s, critical: %s' % (warning_res, critical_res))
        
        if critical_res:
            print(u"\033[41;1mCRITICAL::\033[0mHost[{0}] Service [{1}] Threadhold [{2}] now [{3}]".format(client_service_data['host'], client_service_data['service'],critical_val, item_data ))
        elif warning_res:
            print(u"\033[43;1mWARNINGL::\033[0mHost[{0}] Service [{1}] Threadhold [{2}] now [{3}]".format(client_service_data['host'], client_service_data['service'],critical_val, item_data ))
        else:
            print(u"\033[42;1mNORMAL::\033[0mHost[{0}] Service [{1}] Threadhold [{2}] now [{3}]".format(client_service_data['host'], client_service_data['service'],critical_val, item_data ))

    else:
        pass # string


