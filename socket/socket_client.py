#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import socket
import time

HOST = '192.168.1.112'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
#    cmd = input('cmd > ').strip()
    cmd = raw_input('cmd > ').strip()
#    s.sendall(cmd.encode('utf-8'))
    if cmd.split()[0].lower() == 'get':
        with open(cmd.split()[1], 'wb') as f:
            f.write()
    if len(cmd) == 0:
        continue
    s.sendall(cmd)
    data = s.recv(1024)
#    print('Received %s' % data.decode('utf-8'))
    print(data)
s.close()

