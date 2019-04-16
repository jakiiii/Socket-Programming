#!/usr/bin/python3
"""
This is a simple and very basic sniff tool.
"""

from socket import *

host = "127.0.0.1"

"""
AP_INT means its IPv4 and SOCK_RAW indicates raw socket and 
IPPROTO_ICMP is ICMP (Internet Control Message Protocol) packet.
"""
s = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)  # create raw socket
s.bind((host, 0))  # create connection

"""
setsockopt  -> Set socket option
IPPROTO_IP  -> This IP protocol we using right now
IP_HDRINCL  -> Specific information protocol. Include the Header IP.
"""
s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
print(s.recvfrom(65565))

s.close()
