#!/usr/bin/python3
from socket import *

host = "127.0.0.1"
port = 9999

"""
AP_INT means its IPv4 and SOCK_STREAM indicates TCP and 0 is default protocol
"""
s = socket(AF_INET, SOCK_STREAM, 0)  # create a tcp socket
s.connect((host, port))  # create a connection with server

msg = "Hello, there form the client."
s.send(msg.encode('ascii'))  # As python 3 style we have to encode data, what client send.

r_msg = s.recv(1024)
"""
As python 3 style we have to decode command or data, what server send and we (client) receive.
"""
print(r_msg.decode('ascii'))

s.close()  # connection close
