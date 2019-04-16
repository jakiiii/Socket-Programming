#!/usr/bin/python3
from socket import *

host_port = ("127.0.0.1", 9999)

"""
AP_INT means its IPv4, SOCK_DGRAM indicates UDP and 0 is specific protocol
"""
s = socket(AF_INET, SOCK_DGRAM, 0)
s.bind(host_port)

while True:
    """
    s.recvfrom() is a function which receive connection to the client. This function return two values.
    We give this value name data and adder. data means client data and adder is client address.
    """
    data, adder = s.recvfrom(1024)
    print("[+] Connection established from ", adder)
    print(data.decode('ascii'))

    msg = "I am the UDP server"
    s.sendto(msg.encode('ascii'), adder)  # sendto for udp function

    break

s.close()  # connection close
