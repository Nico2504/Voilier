#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
IP_Serv="192.168.5.254"
PORT=5005
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_Serv,PORT))
while True :
    data, addr=sock.recvfrom(6)
    print data
