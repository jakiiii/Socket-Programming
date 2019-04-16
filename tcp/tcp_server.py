#!/user/bin/python3
from socket import *

host = "127.0.0.1"
port = 9999

"""
AP_INT means its IPv4, SOCK_STREAM indicates TCP and 0 is specific protocol
"""
s = socket(AF_INET, SOCK_STREAM, 0)  # create a tcp socket
s.bind((host, port))  # bind a connection with client
s.listen(5)  # 5 is a integer and its indicate 5 connection we will create at a time.

while True:
    """
    s.accept() means its accept the socket connection and this function return two values.
    We give this value name c and adder. c means client information and adder is client address.
    c.recv() this function return us client information. 1024 means 1024bit par return value.
    """
    c, adder = s.accept()
    r_msg = c.recv(1024)
    """
    In python 3 use the data in ascii. This reason when we receive data then we have to decode data
    and when we send data we have to encode data.
    """
    print(r_msg.decode('ascii'))

    msg = 'Hello, This is the message from server.'
    """
    c.send() function indicates command / data to client then we have to encode the message as python 3 style.
    """
    c.send(msg.encode('ascii'))

    break

c.close()  # connection close
