#!/usr/bin/env python
#better version

from socket import *

HOST = '192.168.1.130'
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZ = 1024

while True:
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  data = raw_input('>')
  if not data:
    break
  #the format should be with a line, server 
  #read as a line from file
  tcpCliSock.send('%s\r\n' % data)
  data = tcpCliSock.recv(BUFSIZ)
  if not data:
    break
  print data.strip()
  tcpCliSock.close()


  
