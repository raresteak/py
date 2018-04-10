#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# minard.py

from datascience import *
import numpy as np

minard = Table.read_table('minard.csv')
print("-------------------------------------------------------")
print("printing table created with csv file")
print(minard)
print("-------------------------------------------------------")
print("Column method")
print(minard.column('Survivors'))
print("-------------------------------------------------------")
print("Select method")
print(minard.select('Survivors'))
print("-------------------------------------------------------")
#Get size of army starting out, element 0 of survivors column/array
initial_army_size = minard.column('Survivors').item(0)
print("-------------------------------------------------------")
print("Intial army size")
print(initial_army_size)
# add a percentage column to right of survivors to see how much the army size had changed.
# create new array
percentage_surviving = minard.column('Survivors') / initial_army_size
print("survivors percentage array")
print(percentage_surviving)
print("-------------------------------------------------------")
# add this new array, percentage_surviving, to a new table
minardWithPercentages = minard.with_column('Percent Surviving', percentage_surviving)

print (minardWithPercentages)
print("-------------------------------------------------------")
#print only row 1 of the minard table
print("take method")
print(minardWithPercentages.take(0))