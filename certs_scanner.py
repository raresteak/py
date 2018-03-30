#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sqlite3, sys, glob, subprocess, re

matches = re.compile(r"""
    Serial\sNumber:.?.?\s+([0-9a-z:]{1,})\s?\(?0?x?[0-9a-z]+\)?.?.?\s?\s+ # Serial Num
    Signature\sAlgorithm:\s(.*)\\n\s+Issuer.* #Public Key Algo
    Validity\\n\s+Not\sBefore:\s+(.*)\s+GMT.* #start date
    Not\sAfter\s?:\s+(.*)\sGMT.* #End date
    Public-Key:\s+\((\d{1,4}) #Key Length

    """, re.VERBOSE)

sqlliteFile = 'certs_scanner.sqlite'

conn = sqlite3.connect(sqlliteFile)
c = conn.cursor()
if len(sys.argv) < 2:
    print("USAGE: certs_scanner.py init|scan")
    sys.exit()

if (sys.argv[1] == "init"):
    print("Initializing sqllite database for first run.")
    c.execute('''CREATE TABLE IF NOT EXISTS sslsigs (
                                id integar PRIMARY KEY,
                                serial_number text NOT NULL,
                                Public_Key_Algorithm text NOT NULL,
                                filename text NOT NULL,
                                filepath text NOT NULL,
                                cn text,
                                key_len int NOT NULL,
                                not_before text,
                                not_after text,
                                first_seen_date text NOT NULL
                                ) ''')
    conn.commit()
    conn.close()
    # Future - Execute a first run after initializing database

elif (sys.argv[1] == "scan"):
    print("Performing scan of SSL certs")
    certList = glob.glob('**/*.crt', recursive=True)
    for cert in certList:
        #print(cert)
        openSSLOutput = subprocess.run(['openssl','x509','-in',cert,'-text',
                                        '-noout'],stdout=subprocess.PIPE)
        #print(openSSLOutput)
        output = matches.findall(str(openSSLOutput))
        print("Serial " + output[0][0] + "\nPublicKeyAlgo " + output[0][1] + 
              "\nkey len " + output[0][4] + "\nStart date " + output[0][2] +
              "\nEnd date " + output[0][3] )
        print("+++++++++++++++++++++++++++++++++++")

elif (sys.argv[1] == "experimental"):
    print("place holder for future option")
else:
    print("USAGE: certs_scanner.py init|scan")