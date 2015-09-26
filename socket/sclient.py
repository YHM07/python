#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

# client

import socket

HOST, PORT = '192.168.1.112', 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = raw_input('>> ')
    if len(cmd.strip()) == 0:
        continue
    s.sendall(cmd)
    if cmd == 'exit':
        break
    res = s.recv(1024)
    print(res)

s.close()


