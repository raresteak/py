#!/usr/bin/env python3
# Finds writable directories on Windows and nix systems
# Author Raresteak
import os
import random
import string
if os.name == 'nt':
    Sep = "\\"
else:
    Sep = "/"
path = input("Enter full directory path to start from: ").rstrip(Sep)
print("Writable directories found from " + path)
tmpFile = "tmp." + str("".join(random.sample(
    string.ascii_uppercase + string.ascii_lowercase + string.digits, 8)))
try:
    testFile = os.path.join(path, tmpFile)
    fh = open(testFile, 'w')
    fh.close()
    print(path)
    os.remove(testFile)
except PermissionError:
    pass
except OSError:
    pass

for (root, dirs, files) in os.walk(path):
    for dir in enumerate(dirs):
        testFile = os.path.join(root, dir[1], tmpFile)
        try:
            fh = open(testFile, 'w')
            testPath = os.path.join(root, dir[1])
            fh.close()
            print(testPath)
            os.remove(testFile)
        except PermissionError:
            pass
        except OSError:
            pass
