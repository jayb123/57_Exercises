#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 09:56:22 2021

@author: jbinstein
"""


#compound interest 

p = int(input("principal: "))

#input must be 1-100 to avoid 
while True:
    try:
        r = int(input("interest rate: "))
        if r < 1 or r > 100:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-100.")


t = int(input("time: "))
n = int(input("compounding periods annually: "))

a = round(p*(1+(r/100)/n)**(n*t),2)

output = "$%s invested at %s for %s year(s) and compounded %s time(s) per year will be worth $%s"%(p,r,t,n,a)

print(output)