#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kill_ie.py

import subprocess, time

def killIE():
    commOut = subprocess.run(["taskkill.exe", "-f", "-IM", "iexplore.exe"])
    return commOut

commOut = killIE()
if commOut.returncode == 0:
    print("explore.exe killed, checking for remaining processes...")
    time.sleep(5)
    commOut = killIE()
    if commOut.returncode > 0:
        print("iexpore killed")
else:
    print("No iexplore processes killed")