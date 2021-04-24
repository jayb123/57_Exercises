#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:59:08 2021

@author: jbinstein
"""
from datetime import date

#create today's date and extracts year
todays_date = date.today()
year = todays_date.year
#user inputs their age and desired retierement age
age = int(input("your age: "))
retirementAge = int(input("target retirement age: "))
#calculates years between current age and retirement age
yearsUntilRetirement = retirementAge - age
year = todays_date.year
retirementYear = year + yearsUntilRetirement

if yearsUntilRetirement > 0:
    print("You have " + str(yearsUntilRetirement) + " until retirement")
    print("It is " + str(year) + " so you can retire in " + str(retirementYear))
else:
    print("You're already retired, what are you using this calculator for?")
