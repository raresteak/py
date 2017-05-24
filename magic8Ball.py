#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  template3.py
#
#  Copyright 2017
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import random
def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber ==2:
		return 'It is decidely so'
	elif answerNumber ==3:
		return 'Yes'
	elif answerNumber==4:
		return 'Reply hazy, try again'
	elif answerNumber==5:
		return 'Ask again later'
	elif answerNumber==6:
		return 'Concentrate and ask again'
	elif answerNumber==7:
		return 'My reply is NO!'
	elif answerNumber==8:
		return 'outlook not so good ;('
	elif answerNumber==9:
		return 'Very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)


