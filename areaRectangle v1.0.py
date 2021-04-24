#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:20:15 2021

@author: jbinstein
"""


#area of a rectangle
import math

width = int(input("what is the width of the room"))
length = int(input("what is the length of the room?"))

area = width * length

output = "The area of the rectangle is " + str(area) + " square feet"

print(output)

areaMeteres = math.sqrt((width**2)*.09290304)*math.sqrt((length**2)*.09290304)

print("or "+ str(areaMeteres) +" Meters")