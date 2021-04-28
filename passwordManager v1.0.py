#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:10:39 2021

@author: jbinstein
"""


#password manager

from getpass import getpass

password = getpass("please choose a password: ")

username = input("Please set your username? ")


print("ten minutes later")

loginUsername = username
loginPassword = getpass("input password for account user %s"%(loginUsername))
  

                  
if password == loginPassword:
    print("Welcome %s"%(loginUsername))
else:
    print("Incorrect Password")    
                  
