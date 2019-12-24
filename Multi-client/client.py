#!/usr/bin/python3


import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((socket.gethostname(),12345))
s.send(bytes("I am CLIENt",'utf-8'))

msg=s.recv(1024)

s.close()
print(msg.decode('utf-8'))