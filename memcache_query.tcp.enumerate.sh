#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Connect to a memcached server and dump key value pairs

####################
# WORK IN PROGRESS #
####################

import socket, re
TCP_IP = "192.168.168.168"
TCP_PORT = 11211
BUFFER_SIZE = 1024

statsItemsRegex = re.compile(r'items:(\d):number')

cacheDumpRegex = re.compile(r'ITEM\s(\S*)\s\[')

# setup connection Ref https://wiki.python.org/moin/TcpCommunication
sock = socket.socket(socket.AF_INET, # Internet
		    socket.SOCK_STREAM) # TCP
sock.connect((TCP_IP, TCP_PORT))
MESSAGE = "stats items\r\n"
sock.send(MESSAGE.encode('utf-8') )
# If you don't add .encode() you get error TypeError: a bytes-like object is required, not 'str'
RESPONSE = sock.recv(BUFFER_SIZE)

for KEYNUM in statsItemsRegex.findall(str(RESPONSE) ):
	#print(KEYNUM)
	MESSAGE2 = str("stats cachedump " + KEYNUM + " 100\r\n")
	#print("Sending: " + MESSAGE2 )
	sock.send(MESSAGE2.encode('utf-8') )
	RESPONSE2 = sock.recv(BUFFER_SIZE) 
	#print("Received..." + str(RESPONSE2) )
	keyName = cacheDumpRegex.findall(str(RESPONSE2) )
	#print(keyName[0])
	MESSAGE3 = str("get keyName[0]\r\n")
	sock.send(MESSAGE3.encode('utf-8') )
	RESPONSE3 = sock.recv(BUFFER_SIZE)
	print(keyName[0] + ":" + str(RESPONSE3) )
sock.shutdown(2)
sock.close()
