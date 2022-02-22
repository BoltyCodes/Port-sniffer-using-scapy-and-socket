import subprocess
import sys

import sock as sock
from scapy.all import *
import socket
from scapy.layers.inet import IP, TCP

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    unlock = []
    try:
        for port in range(2, 1025):
            sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostfound = sockets.connect_ex((IP(dst="192.168.56.1"), port))
            if hostfound == 0:
                ports = print("Port {}: 	 Open".format(port))
            sock.close()
            unlock.append(port)

    except KeyboardInterrupt:
        print
        "You exited this code"
        sys.exit()

    p = IP(dst="192.168.56.1") / TCP(flags="S", sport=RandShort(), dport=unlock)


    s.connect(("192.168.1.254", 80))
    s.send(p)
    p.show()
    print("Request sent!")
except:
    print("An error occurred.")
