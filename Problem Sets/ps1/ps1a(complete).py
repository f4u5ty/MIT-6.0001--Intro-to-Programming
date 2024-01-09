# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:01:31 2022

@author: f4u5t
 
"""

            
starting_salary = float(input("Enter your Salary: "))
portion_saved = float(input("Enter percent to save each month, in decimal form: "))
total_cost = float(input("Enter the total cost of your home: "))
down_payment = total_cost * 0.25
current_savings = 0 
monthly_savings = (starting_salary/12) * portion_saved
r = 0.04
months = 0 
while current_savings < down_payment: 
    current_savings += ((current_savings/12)*r)+monthly_savings 
    months+=1 
print("Number of Months:", months)
  
            
        
    
    
    
