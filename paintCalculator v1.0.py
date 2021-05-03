#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:26:45 2021

@author: jbinstein
"""


#painting a rool
#one gallon = 350sqft

import math

width = int(input("what is the width of the wall"))
length = int(input("what is the length of the wall?"))
gallonCover = 350


gallonsRequired = math.ceil(width * length / gallonCover)


output = "You will need to gather %s gallons of paint"%(gallonsRequired)

print(output)
