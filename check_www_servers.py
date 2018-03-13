#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Check webservers
import urllib.request

WWWPORT='9088'
WWWLIST='servers.txt'  # server/IP one per line
TIMEOUT=2

servers2Check = open(WWWLIST, 'r')

for server in servers2Check:
	WWW = str('https://' + server.strip() + ':' + WWWPORT)
	try:
		CODE = urllib.request.urlopen(WWW,None,TIMEOUT).getcode()
		print(str(CODE) + ':' + WWW )
	except urllib.error.URLError:
		print("Timeout:" + WWW + " HOST DOWN!!!!!!!!!!!!!!!!")
