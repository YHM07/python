#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

# client

import socket

class FTP(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def put(self, msg): # put local_file
        pass

    def get(self, msg): # get remote_file
        print('get msg %s ' % msg)
        if len(msg) > 0:
            remote_file = msg[0]
            cmd_msg = 'file_transfer|get|%s' % remote_file
            self.sock.sendall(cmd_msg)
            feedback = self.sock.recv(1024)
            print('feedback:{0}'.format(feedback))

            if feedback.startswith('file_transfer|get|ready'):
                file_size = feedback.split('|')[-1]
                file_size = int(file_size)
                ack_msg = 'file_transfer|get|recv|ready'
                self.sock.sendall(ack_msg)
                f = file('recv/%s' % remote_file, 'wb')

                recv_size = 0

                while not recv_size == file_size:
                    if file_size - recv_size > 1024:
                        data = self.sock.recv(1024)
                        recv_size += len(data)
                    else:
                        data = self.sock.recv(file_size - recv_size)
                        recv_size += file_size - recv_size

                    f.write(data)
                else:
                    f.close()
                    print('recv file done')



    def list_file(self, msg):
        pass

    def interactive(self):
        while True:
            user_input = raw_input('ftp_cmd ')
            if len(user_input.strip()) == 0:
                continue
            cmd = user_input.split()
            if hasattr(self, cmd[0]):
                func = getattr(self, cmd[0])
                func(cmd[1:])
            else:
                print('\033[31;1mWrong cmd usage!\033[0m')

    def connect(self):
       self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.sock.connect((self.host, self.port))
       self.interactive()


if __name__ == '__main__':
    HOST, PORT = '192.168.1.112', 50007
    ftp = FTP(HOST, PORT)
    ftp.connect()
    ftp.interactive()




