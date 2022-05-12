# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:54:46 2017

@author: uzer
"""

import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = sys.argv.pop() if len(sys.argv) == 2 else '127.0.0.1'
PORT = 1060
s.connect((HOST, PORT))
print('Client has been assigned socket name', s.getsockname())

while True :
    message = input("Enter the message to send or '@' to disconnect : ")
    s.sendall(message.encode())
    reply = s.recv(1024)
    print('The server said', repr(reply))
    end="@"
    if message==end :
        break;
        
reply = s.recv(1024)   
print('The server said', repr(reply))
print("Now your're disconnected from the server ")        
s.close()