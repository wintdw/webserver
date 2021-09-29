# Example server program in Python that serves clients
# with the current server time
import os, sys
import select
import errno
import socket
import time
import multiprocessing
import threading
from datetime import datetime

server = socket.socket();
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR | socket.SO_REUSEPORT, 1)
server.setblocking(0)
server.bind(("127.0.0.1", 40404));
server.listen();

# CPUbound
def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# IObound
def sleep(n):
    time.sleep(n)

def handle(conn, addr):
    p = os.getpid()
    print("{}: [{}] Accepting {}".format(datetime.now(), p, addr))
    conn.send(str(fib(35)).encode())
    #conn.send(str(sleep(4)).encode())
    print("{}: [{}] Processed {}".format(datetime.now(), p, addr))
    conn.close()

#def process():
#    while(True):
#        (conn, addr) = server.accept()
#        handle(conn, addr)
#
#process()

inputs = [server]

while True:
    print(inputs)
    readable, _, _ = select.select(inputs, [], inputs)
    for s in readable:
        connection, client_address = s.accept()
        #handle(connection, client_address)
        threading.Thread(target=handle, args=(connection, client_address,)).start()
        #multiprocessing.Process(target=handle, args=(connection, client_address,)).start()
