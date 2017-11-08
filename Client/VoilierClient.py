#!/usr/bin/env python
# coding: utf-8

import socket

class VoilierClient: #création de la classe VoilierClient

	def __init__(self): #On définit les différents attributs de la classe 
		self.id_trame=0; #stockage de la valeur id_trame
		self.ipserveur=""#stockage de la valeur ipserveur
		self.portserveur=0#stockage de la valeur portserveur
		self.valeurSafran=0#stockage de la valeurSafran
		self.valeurGV=0#stockage de la valeurGV
		self.gite=0#stockage de la valeur gite
		self.lattitude=0#stockage de la valeur de la longitude
		self.longitude=0#stockage de la valeur de la lattitude
		self.vitessevent=0#sotckage de la valeur vitessevent
		self.orientationvent=0#stockage de la valeur orientationvent

	def initCom(self,ipserveur,portserveur): #création de la méthode initCom
		self.ipserveur=ipserveur#récupération de l'adresse IP du serveur
		self.portserveur=portserveur#récupération du port correspondant au serveur
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	#def affichagevaleurs(self,valeurSafran,valeurGV,gite,lattitude,longitude,vitessevent,orientationvent):
	#	print "valeurSafran",self.valeurSafran
	#	print "valeurGV",self.valeurGV
	#	print "gite",self.gite
	#	print "lattitude",self.lattitude
	#	print "longitude",self.longitude
	#	print "vitessevent",self.vitessevent
	#	print "orientationvent",self.orientationvent
	

	def txrx(self): #création de la méthode txrx
		trame = bytearray([self.id_trame,2,self.valeurSafran,self.valeurGV])
		print "--Question-->"
		print "trame Question :", str(trame).encode("hex") #affichage de la trame question
		self.sock.sendto(trame, (self.ipserveur, self.portserveur))
		tramereponse, addr = self.sock.recvfrom(1024)


		b3=ord(tramereponse[4]) #récupération de la valeur
		b2=ord(tramereponse[5]) #récupération de la valeur
		b1=ord(tramereponse[6]) #récupération de la valeur
		b0=ord(tramereponse[7]) #récupération de la valeur

		lattitude=b3<<24|b2<<16|b1<<8|b0#décalage de bit

	   	if b3 > 127:
	   		lattitude=(~lattitude)&0XFFFFFFFF#calcul de la lattitude
	   		lattitude=lattitude+1#incrémentation
	   		lattitude=lattitude*-1#incrémentation


		b7=ord(tramereponse[8]) #récupération de la valeur
		b6=ord(tramereponse[9]) #récupération de la valeur
		b5=ord(tramereponse[10])#récupération de la valeur
		b4=ord(tramereponse[11])#récupération de la valeur

		longitude=b7<<24|b6<<16|b5<<8|b4#décalage de bit

	  	if b7 > 127:
	  		longitude=(~longitude)&0XFFFFFFFF#calcul de la longitude
	  		longitude=longitude+1#incrémentation
	  		longitude=longitude*-1#incrémentation


		self.gite= ord(tramereponse[12])
		self.vitessevent=ord(tramereponse[2])
		self.orientationvent=ord(tramereponse[3])
		self.lattitude=float(lattitude)/10000000#chiffres a virgules
		self.longitude=float(longitude)/10000000#chiffres a virgules

		self.id_trame+=1 #augmente de 1


	

monVoilierClient=VoilierClient()
monVoilierClient.initCom("127.0.0.1",12501)#connexion au serveur avec l'@IP et le port
monVoilierClient.valeurSafran=18;#On définit la valeur du safran
monVoilierClient.valeurGV=65;#On définit la valeur de la grande voile
monVoilierClient.txrx()
print monVoilierClient.lattitude #affichage lattitude
print monVoilierClient.longitude #affichage longitude
print monVoilierClient.gite #affichage gite



