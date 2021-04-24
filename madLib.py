#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:45:17 2021

@author: jbinstein
"""


#entries
noun = input("Enter a Noun: ")
verb = input("Enter a Verb: ")
adjective = input("Enter an Adjective: ")
adverb = input("Enter an Adverb: ")

output = "do you " + verb + " your " + adjective + " "+  noun + " " + adverb  

interpolation = "do you %s your %s %s %s?"%(verb,adjective,noun,adverb)



print(output)
print(interpolation)

  