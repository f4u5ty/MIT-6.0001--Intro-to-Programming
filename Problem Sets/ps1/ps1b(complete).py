# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:27:54 2022

@author: f4u5t
"""
"""
starting_salary = float(input("Enter your Salary: "))
portion_saved = float(input("Enter percent to save each month, in decimal form: "))
total_cost = float(input("Enter the total cost of your home: "))
semi_annual_raise = float(input("Enter your semi-annual riase, in decimal form: "))
down_payment = total_cost * 0.25
current_savings = 0 
monthly_savings = (starting_salary/12) * portion_saved
r = 0.04
months = 0 

while current_savings < down_payment:  
    current_savings += ((current_savings*r)/12)+monthly_savings
    months+=1 
    
    if months%6 == 0: 
        starting_salary += starting_salary*semi_annual_raise
        monthly_savings = (starting_salary * portion_saved)/12 #This needs to be updated???
        #things need to be updated, they don't update themselves, even if original value 
        # is updated
    
print("Number of Months:", months)
"""


salary = float(input("Enter Salary: "))
total_cost = float(input("Enter the cost of your dream: "))
percent_saved = float(input("Enter percentage you save each month (decimal):"))
semi_annual_raise = float(input("Enter semi annual raise (decimal):"))
current_savings = 0 
r = 0.04 
down_payment = total_cost*0.25
months = 0 
monthly_savings = ((salary/12)*percent_saved)
                   
while current_savings < down_payment: 
    months += 1 
    current_savings += monthly_savings + ((current_savings/12)*r)
    if months%6 == 0: 
        salary += (salary*semi_annual_raise)
        monthly_savings = ((salary/12)*percent_saved)
        
print("Number of Months:", months)
print("Current Savings:", current_savings)
