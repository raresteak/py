#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nslookup.py
# Overview: Single run mode: take an ip return result
# Batch mode: take a file with IP on own line

# ToDO: 1. add regex to check for proper formated IP  2. Add ability to lookup fqdn's too.   3. output batch mode to file rather than terminal
#

import sys, socket

if len(sys.argv)-1 == 0:
    print("Lookup IP addresses")
    print("USAGE nslookup.py [ [IP] | [-batch filename] ]")
elif len(sys.argv)-1 == 1:
    toLookUp = sys.argv[1]
    print("Single mode nslookup of " + toLookUp )
    result = socket.gethostbyaddr(toLookUp)
    print(result[0] )

elif len(sys.argv)-1 == 2:
    MODE = sys.argv[1]
    fileName = sys.argv[2]
    if (MODE != '-batch'):
        print("USAGE ERROR nslookup.py [ [IP|FQDN] | [-batch filename] ]")
    print("Batch mode nslookup, using file: " + fileName +"..." )
    with open(fileName) as file_object:
        counter = 0
        for line in file_object:
            result = socket.gethostbyaddr(line)
            print(result[0] )
            counter +=1
    print("Processed " + str(counter) + " lines")
        
else:
    print("Too many command line arguments")
    print("USAGE nslookup.py [ [IP|FQDN] | -batch filename] ]")
