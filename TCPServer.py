# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:45:32 2017

@author: uzer
"""

import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = sys.argv.pop() if len(sys.argv) == 2 else '127.0.0.1'
PORT = 1060
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

print('Listening at', s.getsockname())
sc, sockname= s.accept()
print('We have accepted a connection from', sockname)
print('Socket connects', sc.getsockname(), 'and', sc.getpeername())
while True:
    
    message = sc.recv(1024)
    size = str(len(message))
    reply="Your data was "+size+" bytes"
    print('Message received from client : ', repr(message))
    sc.sendall(reply.encode())
    end="@"
    if message==end.encode() :
       break;

sc.sendall("Conversation Ended".encode())      
sc.close()
print('Reply sent, socket closed')
