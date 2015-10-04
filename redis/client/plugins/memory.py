#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import commands

# def monitor(first, invoke=1):
def monitor(invoke=1):
    monitor_dic = {
            'SwapUsage': 'percentage',
            'MemUsage': 'percentage',
            }

    shell_command = "grep 'MemTotal\|MemFree\|Buffers\|^Cached\|SwapTotal\|SwapFree\|' /proc/meminfo"

    status, result = commands.getstatusoutput(shell_command)

    if status != 0: 
        val_dic = {'status': status}
    else:
        val_dic = {'status': status}
        for i in result.split('kB\n'):
            key = i.split()[0].strip(':') # factor name
            value = i.split()[1]  # factor value
            val_dic[key] = value

        if monitor_dic['SwapUsage'] == 'percentage':
            val_dic['SwapUsage_p'] = str(100 - int(val_dic['SwapFree'] * 100) / int(val_dic['SwapTotal']))
        # real SwapUsage value
        val_dic['SwapUsage'] = int(val_dic['SwapTotal']) - int(val_dic['SwapFree'])
        MemUsage = int(val_dic['MemTotal']) - int(val_dic['MemFree']) + int(val_dic['Buffers']) + int(val_dic['Cached'])
        if monitor_dic['MemUsage'] == 'percentage':
            val_dic['MemUsage_p'] = str(int(MemUsage) * 100 / int(val_dic['MemTotal']))

        # real MemUsage value
        val_dic['MemUsage'] = MemUsage

    return val_dic

