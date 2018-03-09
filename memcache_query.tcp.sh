#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Connect to a memcached server over UDP, retrieve some keys
import socket
TCP_IP = "192.168.168.168"
TCP_PORT = 11211
MESSAGE = "get myteststringkey\r\n"
BUFFER_SIZE = 1024

# setup connection Ref https://wiki.python.org/moin/TcpCommunication
sock = socket.socket(socket.AF_INET, # Internet
		    socket.SOCK_STREAM) # TCP
sock.connect((TCP_IP, TCP_PORT))
sock.send(MESSAGE.encode('utf-8') )
# If you don't add .encode() you get error TypeError: a bytes-like object is required, not 'str'
RESPONSE = sock.recv(BUFFER_SIZE)
#sock.shutdown()
sock.close()
print("Received..." + str(RESPONSE) )
