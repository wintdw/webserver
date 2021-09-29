# Example client program in Python that receives the current server time
import socket
import os
from datetime import datetime
from multiprocessing import Process

serverIP    = "127.0.0.1";
serverPort  = 40404;

def clientConnect(ip, port):
    p = os.getpid()
    tcpSocket   = socket.socket();
    print("{}: [{}] Connecting {}:{}".format(datetime.now(), p, ip, port))
    tcpSocket.connect((ip, port));
    
    print("{}: [{}] Receiving {}:{}".format(datetime.now(), p, ip, port))
    received = tcpSocket.recv(1024);
    print(received)

for i in range(10):
    Process(target=clientConnect, args=(serverIP, serverPort,)).start()
