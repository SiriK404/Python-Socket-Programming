
# import socket programming library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()  #to lock the thread

# thread function
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
            # lock released on exit
            print_lock.release()
            break

        print(data)


        # send back same data string to client
        c.send(bytes("hello " + str(data), 'utf-8'))

        # connection closed
    c.close()


def Main():
    host = ""


    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()



        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        print_lock.acquire()
        start_new_thread(threaded, (c,))

    s.close()


if __name__ == '__main__':
    Main()
