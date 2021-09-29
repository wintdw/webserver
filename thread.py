# Example server program in Python that serves clients
# with the current server time
import socket
import time
from datetime import datetime
import threading
import os 

serverSocket = socket.socket();
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(("127.0.0.1", 40404));
serverSocket.listen();

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
    #conn.send(str(fib(35)).encode())
    conn.send(str(sleep(4)).encode())
    print("{}: [{}] Processed {}".format(datetime.now(), p, addr))
    conn.close()

def process():
    while(True):
        (conn, addr) = serverSocket.accept()
        handle(conn, addr)

threads = []
for i in range(4):
    t = threading.Thread(target=process)
    threads.append(t)
    t.start()
