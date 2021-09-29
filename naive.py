# Example server program in Python that serves clients
# with the current server time
import os, sys
import socket
from datetime import datetime
import multiprocessing

serverSocket = socket.socket();
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(("127.0.0.1", 40404));
serverSocket.listen();

def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def handle(conn, addr):
    p = os.getpid()
    print("{}: [{}] Accepting {}".format(datetime.now(), p, addr))
    conn.send(str(fib(35)).encode())
    print("{}: [{}] Processed {}".format(datetime.now(), p, addr))
    conn.close()

def process():
    while(True):
        (conn, addr) = serverSocket.accept()
        handle(conn, addr)

process()
