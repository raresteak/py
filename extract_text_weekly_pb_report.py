#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Create a formated csv file from the weekly pb email reports
# 

import pyperclip, re

reportLineRegex = re.compile(r"""
							\s*
							(\S*)		# Match1=servername
							\s*
							(\[.*\])	# Match2=date
							\s*
							(\w\d*)		# Match3=id
							\s*
							(\w*\s\w*)	# Match3=name
							\s*""", re.VERBOSE)							
'''
#example email report:
                         iislab [Thu Dec 21 13:50:27 2017] z1234569         Mr Wilson                   
   servUbun001.lab.dom [Mon Dec 18 20:38:06 2017] y123         Paul Smith                    
   proxyWin.lab.co [Tue Dec 19 21:44:58 2017] h9090         Sally Johns                                       
'''
# Grab the clipboard
text = str(pyperclip.paste())

# Find results using compiled regex
results = reportLineRegex.findall(text)
# results contains a list of tuples

# output to file
outputfile = open('pbreport.csv', 'w')

#create a header for csv file.
outputfile.write("hostname,dates,id,real_name\n")

# print what I want	to screen and to a file
for hostname,date,id,name in results:
	myLine=str(hostname + ',' + date + ',' + id + ',' + name)
	print(myLine)
	outputfile.write(myLine + '\n')