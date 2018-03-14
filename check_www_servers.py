#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Check webservers
import urllib.request, os

WWWPORT='9088'
WWWLIST='servers.txt'
TIMEOUT=2

servers2Check = open(WWWLIST, 'r')

for server in servers2Check:
	WWW = str('https://' + server.strip() + ':' + WWWPORT)
	try:
		CODE = urllib.request.urlopen(WWW,None,TIMEOUT).getcode()
		print(str(CODE) + ':' + WWW + " UP!")
	except urllib.error.URLError:
		print("Timeout connecting to: " + WWW + "   Port:" + WWWPORT + " down!")
		print("Trying to ping host:...")
		pingHost=str('ping -n 1 ' + server.strip())
		if not os.system(pingHost):
			# If return code 0, successful ping
			print("Host up, reponds to ping")
		else:
			# return is 1, ping failed
			print("Host down!!!")
