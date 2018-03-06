#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# create a file with epoch time in name

import time

filename=('testfile.' + str(int(time.time() * 1000)) + '.txt')

outputfile = open(filename, 'w')