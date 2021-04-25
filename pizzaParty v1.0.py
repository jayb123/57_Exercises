#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:10:36 2021

@author: jbinstein
"""


#pizza party

peopleCount = int(input("How many people: "))
pizzaCount = int(input("How many pizzas: "))
sliceCount = int(input("How Many Slices Per Pizza: "))


slicesPerPerson = sliceCount * pizzaCount // peopleCount
leftovers = sliceCount * pizzaCount % peopleCount

print(leftovers)



output1 = "There are " + str(peopleCount) + " people and there are " + str(pizzaCount) + " pizzas"


output2 = "each person gets " + str(slicesPerPerson) + " slices of Pizza"

if leftovers==1:
    output3 = "There is %s slice of pizza leftovers"%(leftovers) #string interpolation
else:
    output3 = "There are %s slices of pizza leftovers"%(leftovers) #string interpolation

print(output1)
print(output2)
print(output3)