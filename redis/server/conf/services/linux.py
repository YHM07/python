#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

from generic import BaseService

class CPU(BaseService):
    
    def __init__(self):
        super(CPU, self).__init__()
        self.interval = 30 
        self.name = 'linux_cpu'
        self.plugin_name = 'get_cpu_status'
        self.triggers = {
                'idle': {
                    'func'     : 'avg',
                    'last'     : 10*60,   # 10 minutes
                    'count'    : 1,
                    'operator' : 'lt',
                    'warning'  : 20,
                    'critical' : 5,
                    'data_type': float,
                    },
                'iowait': {
                    'func'     : 'hit',
                    'last'     : 15*60,   # 10 minutes
                    'count'    : 5,
                    'operator' : 'gt',
                    'warning'  : 40,
                    'critical' : 50,
                    'data_type': float,
                    
                    },
                }

class Memory(BaseService):
    def __init__(self):
        super(Memory, self).__init__()
        self.interval = 20 
        self.name = 'linux_memory'
        self.plugin_name = 'get_memory_status'
        self.triggers = {
                'usage': {
                    'func'     : 'avg',
                    'last'     : 5*60,
                    'count'    : 1,
                    'operator' : 'gt',
                    'warning'  : 80,
                    'critical' : 90,
                    'data_type': float,
                    },
                }

class Network(BaseService):
    def __init__(self):
        super(Network, self).__init__()
        self.interval = 60 
        self.name = 'linux_network'
        self.plugin_name = 'get_network_status'
        self.triggers = {
                'in': {
                    'func'     : 'hit',
                    'last'     : 10*60,
                    'count'    : 5,
                    'operator' : 'gt',
                    'warning'  : 1024*1024*10, # 10*1M
                    'critical' : 1024*1024*15, # 15*1M
                    'data_type': float,
                    },
                'out': {
                    'func'     : 'hit',
                    'last'     : 10*60,
                    'count'    : 5,
                    'operator' : 'gt',
                    'warning'  : 1024*1024*10, # 10*1M
                    'critical' : 1024*1024*15, # 15*1M
                    'data_type': float,
                    },
                }
