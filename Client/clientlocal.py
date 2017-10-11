#!/usr/bin/env python
# coding: utf-8

import socket


#ip = "192.168.0.225" #Com Raspi
ip = "127.0.0.1"
port = 12501


trame = bytearray([51,8,30,45,30])
print "--Question-->"
print "trame Question :", str(trame).encode("hex")

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.sendto(trame, (ip, port))


tramereponse, addr = sock.recvfrom(1024)

print "--Réponse-->"
print "trame de réponse:",tramereponse.encode("hex")
print "ID=",ord(tramereponse[0])#affichage de l'octet 0
print "Lg=",ord(tramereponse[1])#affichage de l'octet 1
print "V.Vent=",ord(tramereponse[2])#affichage de l'octet 2
print "D.Vent=",ord(tramereponse[3])#affichage de l'octet 3
print "Gite=", ord(tramereponse[12])#affichage de l'octet 4
b3=ord(tramereponse[4])<<24
b2=ord(tramereponse[5])<<16
b1=ord(tramereponse[6])<<8
b0=ord(tramereponse[7])<<0
print "lattitude", b3+b2+b1+b0


b7=ord(tramereponse[8])<<24
b6=ord(tramereponse[9])<<16
b5=ord(tramereponse[10])<<8
b4=ord(tramereponse[11])<<0
print "longitude", b7+b6+b5+b4