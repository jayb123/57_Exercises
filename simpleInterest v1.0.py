#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:53:03 2021

@author: jbinstein
"""


#computing simple interest

principal = int(input("Enter the principal amount: "))
intRate = int(input("Enter the Interest Rate: "))
yearAccrued = int(input("Enter the years you will invest: "))

endAmount = round(principal*(1+(intRate/100) * yearAccrued),2)

print("You will have $" + str(endAmount))

#challenges
#ensure numeric entry
#print amount at end of each year
