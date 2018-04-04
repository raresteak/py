#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# port_scanner.py
# Original code: http://www.coderholic.com/python-port-scanner/ 
# Thank you coderholic
# 
# Made a couple changes from original design.
# 1. Changed code to run under Python3, commented below.
# 2. Added try/except for handling bad NS lookups, commented below
# 3. Changed for loop to target specific ports, commented below
# 4. Added print for closed ports, commented below.

# To do
# 1. Add batch mode 

from socket import * 
# explanaition of above import
# https://stackoverflow.com/questions/24872125/socket-import-does-not-work-from-does-whats-the-deal


# Updated input for python3
target = input('Enter fqdn to scan: ')

# Adding code to catch fqdn's that are unresolvable.
try:
    targetIP = gethostbyname(target)
except Exception as errorMsg:
    print ("ERROR: Bad FQDN: " + target)
    # capturing exception https://docs.python.org/3/tutorial/errors.html
    print ("Exception was {0}".format(errorMsg) )
    exit(1)

# updated print for python3
print ('Starting scan on host ', targetIP)

#scan reserved ports
#for i in range(20, 1025):
# scan specif ports, if doing range comment out for statement below, uncomment above range
for i in [3389, 389, 445, 446]:
    s = socket(AF_INET, SOCK_STREAM)

    result = s.connect_ex((targetIP, i))

    if(result == 0) :
        # updated print for python3
        print ('Port ' + str(i) + ': ' + 'OPEN')
    # added by me
    # comment out next two lines if you don't want to see list of closed ports
    else:
        print ('Port ' + str(i) + ': ' + 'CLOSED...result code: ' + str(result))
    s.close()