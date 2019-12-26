import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',1000))
s.send(bytes("I am client",'utf-8'))

msg=s.recv(4096)

print(msg.decode('utf-8'))
s.send(bytes("how is the weather?",'utf-8'))
msg=s.recv(4096)


print(msg.decode('utf-8'))
s.close()
