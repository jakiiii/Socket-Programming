#!/usr/bin/python3
from socket import *

host_port = ("127.0.0.1", 9999)

"""
AP_INT means its IPv4, SOCK_DGRAM indicates UDP and 0 is default protocol
"""
s = socket(AF_INET, SOCK_DGRAM, 0)

msg = "I am the UDP client"
s.sendto(msg.encode('ascii'), host_port)  # sendto for udp function

data, adder = s.recvfrom(1024)
print(data.decode('ascii'))

s.close()  # connection close
