#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:36:19 2021

@author: jbinstein
"""


#Legal Driving Age

age = int(input("How old are you?: "))

if age >= 16:
    dec = "You can drive"
else:
    dec = "you're too young"


#ternary operator
    
decTernary = "you can drive" if age >= 16 else "you're too young"


print(dec)

print(decTernary)