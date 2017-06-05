#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  guessTheNumber.py
#  
#  Copyright 2017 Unknown <jar@blue>
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


def main(args):
    import random
    secretNumber = random.randint(1,20)
    print('I am thinking of a number betwen 1 and 20.')
    for guessesTaken in range(1,7):
		print('Take a guess')
		guess=int(input())
		
		if guess < secretNumber:
			print('Your guess is too low')
		elif guess > secretNumber:
			print('Your guess is too high')
		else:
			break
    if guess == secretNumber:
        print('Good job! You guessed by number in ' + str(guessesTaken) + ' guessess!')
    else:
        print('Nope. the number I was thinking of was ' + str(secretNumber))
		
	
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
