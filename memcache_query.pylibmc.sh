#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Connect to a memcached server over UDP, retrieve some keys
import pylibmc
# Setup connection
#TCP
#MEMCONN = pylibmc.Client(["192.168.168.168"], binary=True )
#UDP con
MEMCONN = pylibmc.Client(["udp:192.168.168.168"])
# Populate data
MEMCONN["myteststringkey"] = "The quick brown fox jumps over the lazy dog"

# Retreive the data 100 times
#for num in range(1000):
RET_DATA = MEMCONN["myteststringkey"]
print(RET_DATA)

'''
pylibmc has not implemented udp connections
$ ./memcache_query.pylibmc.sh 
Traceback (most recent call last):
  File "./memcache_query.pylibmc.sh", line 14, in <module>
    RET_DATA = MEMCONN["myteststringkey"]
  File "/usr/local/lib/python3.5/dist-packages/pylibmc/client.py", line 158, in __getitem__
    value = self.get(key, _MISS_SENTINEL)
pylibmc.NotSupportedError: error 28 from memcached_get(myteststringkey): (0x20f87a0) ACTION NOT SUPPORTED -> libmemcached/get.cc:216

'''
