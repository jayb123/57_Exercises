#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 08:57:29 2021

@author: jbinstein
"""
    
        
NewDictionary = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",\
7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

def monthName(monthNumber): 
    return NewDictionary.get(monthNumber, 'Month not found!')       

monthNumber= int(input("Enter number "))
print(monthName(monthNumber))      
    

        
        