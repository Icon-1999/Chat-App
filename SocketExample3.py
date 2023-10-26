import socket
import sys
import select

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 4445))

while True:
    readers, _, _ = select.select([sys.stdin], [], [])
    for reader in readers:
        if reader is c:
            print(c.recv(1000).decode('utf-8'))
        else:
            mgs = sys.stdin.readline()
            c.send(mgs.encode('utf-8'))