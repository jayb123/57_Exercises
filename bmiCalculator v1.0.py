# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#BMI Calculator

weight = int(input("weight in pounds"))

height = int(input("height in inches"))


bmi = round((weight/(height**2))*703,2)

if bmi > 18.5 and bmi < 25:
    result = "healthy"
    action = "should keep up the good work"
elif bmi < 18.5:
    result = "Underweight"
    action = "may want to increase your calorie intake"
else:
    result = "overweight"
    action = "may want to diet"

output = "Your bmi is %s a %s number, so you %s"%(bmi,result,action)
    
print(output)
