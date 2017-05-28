#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  commaList.py
#  
#  Copyright 2017 - <->
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
# Chap 4 Q1
#Write a function that takes a list value as an argument and returns
#a string with all the items separated by a comma and a space, with and
#inserted before the last item. For example, passing the previous spam list to
#the function would return 'apples, bananas, tofu, and cats' . But your func-
#tion should be able to work with any list value passed to it.
def main(args):
    spam = ['apples', 'bananas', 'tofu', 'cats']
    #spam = ['apples', 'bananas', 'tofu', 'cats', 'turtles']
    for i in range(len(spam)):
        if i == (len(spam)- 1):
            print(' and ' + spam[i] + '!!!!')
        else:    
            print(spam[i] + ', ', end="")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
