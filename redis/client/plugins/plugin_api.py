#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import load, memory
# import cpu

# def get_load_status():
#     return load.monitor()

def get_network_status():
    return load.monitor()

# def get_cpu_status():
#     return cpu.monitor()

def get_memory_status():
    return memory.monitor()
