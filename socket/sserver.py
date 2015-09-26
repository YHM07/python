#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

# server

# import socket
import SocketServer
import os

class MyTCPHandle(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            self.cmd = self.request.recv(1024).strip()
            print('Connected by {0}:{1}'.format(self.client_address[0],
                self.client_address[1]))
            if not self.cmd:
                break
            if self.cmd == 'exit':
                break
            cmd_res = os.popen(self.cmd).read()
            self.request.sendall(cmd_res)

if __name__ == '__main__':

    HOST, PORT = '0.0.0.0', 50007
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandle)
    server.serve_forever()    


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(1)
# while True:
#     conn, addr = s.accept()
#     print('Connected by {0}:{1}'.format(addr[0], addr[1]))
#     while True:
#         cmd = conn.recv(1024)
# #       if not cmd:
# #           break
#         if cmd == 'exit':
#             break
#         conn.sendall(cmd.upper())
# 
#     conn.close()


