#!/usr/bin/env python

import socket
IP_CLIENT="192.168.0.225"
PORT=12800

socketserveur=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketserveur.sendto("Salut",(IP_CLIENT,PORT))

print 'Envoye'
