#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:11:04 2021

@author: jbinstein
"""


#comparing numbers

first = int(input("first: "))
second = int(input("second: "))
third = int(input("third: "))

if first == second or first == third or second == third:
    print("no two can be the same")
else:
    print(max(first,second,third))
    
## challenge write algorithm don't use max

'''
#comparing numbers

first = int(input("first: "))
second = int(input("second: "))
third = int(input("third: "))

if first == second or first == third or second == third:
    print("no two can be the same")
else:
   if first > second and first > third:
       print(first)
   elif second > third:
       print(second)
   else:
       print(third)
 '''
