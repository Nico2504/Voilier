#!/usr/bin/env python
# coding: utf-8

import socket


ip = "192.168.0.225" #Com Raspi
#ip = "127.0.0.1"
port = 12501


trame = bytearray([51,42,36,25])
print "--Question-->"
print "trame question :", str(trame).encode("hex")

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.sendto(trame, (ip, port))


data, addr = sock.recvfrom(5)

print "<--Réponse--"
print "ID=",ord(data[0])
print "Lg=",ord(data[1])
print "V.Vent=",ord(data[2])
print "D.Vent=",ord(data[3])
print "Gite=", ord(data[4])
