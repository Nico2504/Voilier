#!/usr/bin/env python
# coding: utf-8

import socket

#ip = "192.168.0.227" #Com Raspi
ip = "127.0.0.1"
port = 12500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

while True:
    data, addr = sock.recvfrom(5)

    print "--Question-->"
    print "UDP Target IP :", ip
    print "UDP Target Port :", port
    print "ID=",ord(data[0])
    print "Lg=",ord(data[1])
    print "GV=",ord(data[2])
    print "Sf=",ord(data[3])
    

    trame1 = bytearray([51,4,30,45,30])
    print "<--Réponse--"
    print "trame réponse :" , str(trame1).encode("hex")


    sock.sendto(trame1,addr)
