#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Random Private IP generator
# Needed for a later project
import random
# Randomly choose 10, 169, 172 or 192

# Once chosen.  pick random octets within range
RANGE = random.choice([10,172,192,169])

# 10.0.0.1 - 10.255.255.254
if RANGE == 10:
    OCT2 = random.randrange(1,255)
    OCT3 = random.randrange(1,255)
    OCT4 = random.randrange(1,254)
    print( str(RANGE) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) )

# 172.16.0.1 - 172.31.255.254
if RANGE == 172:
    OCT2 = random.randrange(16,31)
    OCT3 = random.randrange(1,255)
    OCT4 = random.randrange(1,254)
    print( str(RANGE) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) )

# 192.168.0.1 - 192.168.255.254
if RANGE == 192:
    OCT2 = 168
    OCT3 = random.randrange(1,255)
    OCT4 = random.randrange(1,254)
    print( str(RANGE) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) )

# Link local
if RANGE == 169:
    OCT2 = 254
    OCT3 = random.randrange(1,255)
    OCT4 = random.randrange(1,254)
    print( str(RANGE) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) )