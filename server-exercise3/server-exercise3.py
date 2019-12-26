import socket
from _thread import *
import threading



print_lock = threading.Lock()
no_of_conn = input("Please enter the number of client connections: ")

def connect_client(conn):

    while True:
        data= conn.recv(4096)
        print(str(data))
        if not data:
            print('Bye')
            # lock released on exit
            print_lock.release()
            break
        conn.send(bytes("hello " + str(data), 'utf-8'))
        data1 = conn.recv(4096)
        a=data1.decode('utf-8')
        if str(a)=='how is the weather?':
            conn.send(bytes(" Its cold and dry,need a hot drink ", 'utf-8'))

        else:
            print_lock.release()
            break



def main():
    ip='127.0.0.1'
    port=1000
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen(5)
    print("server is listening:")



    while True:

        conn,addr=s.accept()
        print("connection is established from " )
        print_lock.acquire()

        start_new_thread(connect_client,(conn,))


    s.close()

if __name__ == '__main__':
    main()
