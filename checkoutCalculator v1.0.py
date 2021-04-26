#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:03:03 2021

@author: jbinstein
"""


#selfCheckout


item = input("item: ")
price = int(input("Price: "))
Quantity = int(input("Quantity: "))
taxRate = .055

cost = round(price * Quantity * (1+taxRate),2)

output = "your %ss cost $%s...enjoy!!!"%(item,cost)

print(output)
                     
        
    

