# Example client program in Python that receives the current server time
import socket
import errno
import select
from datetime import datetime
from multiprocessing import Process

serverIP    = "127.0.0.1";
serverPort  = 40404;

def clientConnect(ip, port):
    tcpSocket   = socket.socket();
    print("{}: Connecting {}:{}".format(datetime.now(), ip, port))
    tcpSocket.connect((ip, port));
    tcpSocket.setblocking(0)
    try:
        tcpSocket.recv(1024);
    except Exception as e:
        if e.errno == errno.EAGAIN:
            select.select([tcpSocket], [], [])

for i in range(10):
    Process(target=clientConnect, args=(serverIP, serverPort,)).start()
