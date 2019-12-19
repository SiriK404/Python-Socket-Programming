#!/usr/bin/python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 4444))
s.listen(5)

while True:
    clientsocket, addr = s.accept()
    
    while True:
        data = clientsocket.recv(4096)
        if not data: break
        
        print(data)
        clientsocket.send(bytes("hello "+ str(data),'utf-8'))
    clientsocket.close()
    print ('client disconnected')
