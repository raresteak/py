#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Random Private IP generator
# Needed for a later project
import random
# Randomly choose 10, 172 or 192

# Once chosen.  pick random octets within range
CLASS = random.choice([10,172,192,169])

# 10.0.0.1 - 10.255.255.254
if CLASS == 10:
    OCT1 = random.randrange(1,255)
    OCT2 = random.randrange(1,255)
    OCT3 = random.randrange(1,254)
    print( str(CLASS) + "." + str(OCT1) + "." + str(OCT2) + "." + str(OCT3) )

# 172.16.0.1 - 172.31.255.254
if CLASS == 172:
    OCT1 = random.randrange(16,31)
    OCT2 = random.randrange(1,255)
    OCT3 = random.randrange(1,254)
    print( str(CLASS) + "." + str(OCT1) + "." + str(OCT2) + "." + str(OCT3) )

# 192.168.0.1 - 192.168.255.254
if CLASS == 192:
    OCT1 = 168
    OCT2 = random.randrange(1,255)
    OCT3 = random.randrange(1,254)
    print( str(CLASS) + "." + str(OCT1) + "." + str(OCT2) + "." + str(OCT3) )

# Link local
if CLASS == 169:
    OCT1 = 254
    OCT2 = random.randrange(1,255)
    OCT3 = random.randrange(1,254)
    print( str(CLASS) + "." + str(OCT1) + "." + str(OCT2) + "." + str(OCT3) )