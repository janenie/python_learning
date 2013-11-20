#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
tcpSocket.listen(5)

while True:
  print 'Waiting for connection...'
  tcpCliSock, addr = tcpSocket.accept()
  print '...connected from: ', addr
  
  while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
      break;
    tcpCliSock.send('[%s] %s' %(
      ctime(), data))
    
  tcpCliSock.close()
  
tcpSocket.close()
  