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
            data = self.request.recv(1024).strip()
            data = data.split('|')
            if hasattr(self, data[0]):
                func = getattr(self, data[0])
                func(data[1:])

    def file_transfer(self, msg):
        if msg[0] == 'get':
            print('going to send file: {0} to client'.format(msg[1]))
            filename = msg[1]
            if os.path.isfile(filename):
                file_size = os.path.getsize(filename)
                ack_msg = 'file_transfer|get|ready|%s' % file_size
                self.request.sendall(ack_msg)
                client_ack = self.request.recv(1024)
                print('client_ack:{0}'.format(client_ack))

                if client_ack.startswith('file_transfer|get|recv|ready'):
                    f = file(filename, 'rb')
                    for line in f:
                        self.request.send(line)
                    else:
                        print('file %s transfer done' % filename)
                        f.close()
            else:
                ack_msg = 'file_transfer|get|file does not exist'
                self.request.sendall(ack_msg)



if __name__ == '__main__':

    HOST, PORT = '0.0.0.0', 50007
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandle)
    server.serve_forever()    


