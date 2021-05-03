#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:40:19 2021

@author: jbinstein
"""


#multistate sales tax calculator


billAmount = int(input("Bill Amount:"))
state = input("what state?:" )
if state.upper() == "WI" or state.upper() == "WISCONSIN":
    tax = .1
    county = input("What county?:")
    if county.upper() == "EAU CLAIRE":
        tax += .005
    elif county.upper() == "DUNN":
        tax += .004
elif state.upper() == "IL" or state.upper() == "ILLINOIS":
    tax = .08
else:
    tax = 0


totalBill = billAmount*(1+tax)

print(totalBill)
