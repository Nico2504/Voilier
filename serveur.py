#!/usr/bin/env python

import socket
IP_SERV="192.168.0.225"

socketserveur=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketserveur.bind((IP_SERV,PORT))

while True:
    data,addr=sock.recvfrom(6)
    

print data
