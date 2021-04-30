#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:29:00 2021

@author: jbinstein
"""


#temperature converter

T = int(input("what is the temperature?"))

unitConvert = input("entered in celcius of farenight [C/F]")

converted = (T-32)*5/9 if unitConvert.upper() == "F" else (T*9/5) + 32
    
output = str(converted) + "C" if unitConvert.upper() == "F" else str(converted) + "F"

print(output)    


