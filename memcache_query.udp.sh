#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Connect to a memcached server over UDP, retrieve some keys
import socket
UDP_IP = "192.168.168.168"
UDP_PORT = 11211
MESSAGE = "get myteststringkey\r\n"

# setup connection Ref https://wiki.python.org/moin/UdpCommunication
sock = socket.socket(socket.AF_INET, # Internet
		    socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))



