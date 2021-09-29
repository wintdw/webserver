# Example server program in Python that serves clients
# with the current server time
import os, sys
import socket
import asyncio
import time
from datetime import datetime

# CPUbound
async def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (await fib(n-1)) + (await fib(n-2))

# IObound
async def sleep(n):
    await asyncio.sleep(n)

async def handle(conn, addr):
    p = os.getpid()
    print("{}: [{}] Accepting {}".format(datetime.now(), p, addr))
    #await loop.sock_sendall(conn, str(await sleep(4)).encode())
    await loop.sock_sendall(conn, str(await fib(35)).encode())
    print("{}: [{}] Processed {}".format(datetime.now(), p, addr))
    conn.close()

async def start_server():
    server = socket.socket();
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR | socket.SO_REUSEPORT, 1)
    server.setblocking(False)
    server.bind(("127.0.0.1", 40404));
    server.listen();

    while(True):
        print( asyncio.all_tasks() )
        conn, addr = await loop.sock_accept(server)
        loop.create_task(handle(conn, addr))

loop = asyncio.get_event_loop()
loop.set_debug(True)
loop.run_until_complete(start_server())
