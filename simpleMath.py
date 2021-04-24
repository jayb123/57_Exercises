#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:47:12 2021

@author: jbinstein
"""


firstNum = int(input("what is the first number?"))
secondNum = int(input("what is the second number?"))

addition = firstNum + secondNum
subtraction = firstNum - secondNum
multiplication = firstNum * secondNum
division = firstNum / secondNum

print(
      str(firstNum) + "+" + str(secondNum) + "=" + str(addition) + "\n"+    
      str(firstNum) + "-" + str(secondNum) + "=" + str(subtraction) + "\n"+  
      str(firstNum) + "*" + str(secondNum) + "=" + str(multiplication) + "\n"+  
      str(firstNum) + "/" + str(secondNum) + "=" + str(division)
      )