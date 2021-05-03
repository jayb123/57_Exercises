#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:34:44 2021

@author: jbinstein
"""


#currency conversion

amountFrom = int(input("How many euros are you trying to convert?:" ))

rateFrom = 1.21
RateTo = 1

amountTo =  round((amountFrom*rateFrom)/RateTo,2)

output = "At the exchange rate of %s Euros per Dollar - your %s Euros\
converts to %s USD"%(rateFrom,amountFrom,amountTo)

print(output)


#challenges
#build a dictionary of conversion rates and prompt for country
#connect to an external API that provides the rates
