#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rot13.py
# Map upper case A-Z to N-ZA-M and lower case a-z to n-za-m
# reference: https://en.wikipedia.org/wiki/ROT13
# Test pattern "The Quick Brown Fox Jumps Over The Lazy Dog"
# Output Gur Dhvpx Oebja Sbk Whzcf Bire Gur Ynml Qbt
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha13=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
import sys

if len(sys.argv)-1 != 1:
	print("Enter some text as argument to script.")	
	sys.exit()
	
myInput = sys.argv[1]

for singleChar in myInput:
	try:
		alphaPosition=alpha.index(singleChar)
	except ValueError:    # Exception handling, catches all special characters and just prints them.
		print(singleChar, end="")
	else:
		print(alpha13[alphaPosition], end="")
		
print('\n' + 'rot13 complete.' )