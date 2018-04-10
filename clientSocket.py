#!/usr/bin/env python
# coding=utf-8
from socket import *
HOST='localhost'
PORT = 21567
BUFFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSocket = socket(AF_INET, SOCK_STREAM)
tcpCliSocket.connect(ADDR)
while True:
    data = raw_input('>')
    if not data:
        break
    tcpCliSocket.send(data)
    data = tcpCliSocket.recv(BUFFSIZ)
    if not data:
        break
    print data
tcpCliSocket.close()

