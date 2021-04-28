#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:42:42 2021

@author: jbinstein
"""


#Tax Calc - State Tax

orderAmount = int(input("What is the order amount?"))
stateCode = input("What is the state code?: ")
salesTax = .05


if stateCode.upper() == "WI" or "WISCONSIN":
    billAmount = orderAmount * (1+salesTax)
else:
    billAmount = orderAmount
        
print(billAmount)
