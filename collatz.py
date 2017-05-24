#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
def collatz(checkNum):
	if checkNum % 2 == 0:
		newNum = checkNum // 2
		#print('Entered EVEN branch, value is now: ' + str(newNum) )
		return newNum
	else:
		newNum = 3 * checkNum +1
		#print('Entered ODD branch, value is now: ' + str(newNum) )
		return newNum

def numLoops(Looper):
	Looper = Looper + 1
	return Looper

def main(args):
	 myCnts = 0
	 print('Collatz Conjecture - Enter a number: ')
	 print('Hint, use 9780657630 produces the largest number of Collatz steps')
	 myNum = int(input())
	 # add check for negative and strings and throw error
	 while myNum != 1:
		 myCnts = numLoops(myCnts)
		 myNum = collatz(myNum)
		 print('Result: '+ str(myNum))
	 print('collatz steps: ' + str(myCnts))
	 # The longest progression for any initial starting number less than 100 million is 
	 # 63,728,127, which has 949 steps. 
	 # For starting numbers less than 1 billion it is 670,617,279, with 986 steps, and for 
	 # numbers less than 10 billion it is 9,780,657,630, with 1132 steps
	 # source: http://en.wikipedia.org/wiki/Collatz_conjecture
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
