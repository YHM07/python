#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import socket
import os
import commands
import SocketServer 

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            self.cmd = self.request.recv(1024)
            print('{0} from {1}'.format(self.cmd, self.client_address))
            if not self.cmd:
                print('client {0} is dead'.format(self.client_address) )
                break
            cmd_status, cmd_result = commands.getstatusoutput(self.cmd)
            if len(cmd_result.strip()):
                self.request.sendall(cmd_result)
            else:
                self.request.sendall('DONE')


# HOST = ''           # Symbolic name meaning all acailable interfaces
# PORT = 50007

if __name__ == '__main__':
    HOST, PORT = '', 50007
    server = SocketServer.ThreadingTCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(1)
# 
# while True:
#     conn, addr = s.accept()
#     print('Connected by {0}'.format(addr))
#     while True:
#         cmd = conn.recv(1024)
#         if not cmd:
#             break
#         print('command from {0}'.format(addr))
# #        os.system(cmd)
# #        cmd_result = os.popen(cmd.decode('utf-8')).read()
# #        cmd_result = os.popen(cmd).read()
# #        cmd_status, cmd_result = commands.getstatusoutput(cmd)
#         cmd_result = os.popen(cmd + ';echo $?').read()
#         if cmd_result == '0\n':
#             conn.sendall('DONE')
#         else:
#             conn.sendall(cmd_result[:-2])
# 
# #        if len(cmd_result.strip()):
# #            conn.sendall(cmd_result)
# #        else:
# #            conn.sendall('DONE')
# 
# #        conn.sendall(cmd_result.encode('utf-8'))
# #        conn.sendall(cmd_result)
# conn.close()
