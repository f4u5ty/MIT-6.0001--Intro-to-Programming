# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:38:38 2022

@author: f4u5ty
"""
r = 0.04 
high = 10000
low = 0 
epsilon = 100 
semi_ann_raise = 0.07 
cost_of_dream = 1000000
down_payment = 0.25 * cost_of_dream 
months = 0 #Needs to be reinitialized every 36
monthly_savings = 0 
step_counter = 0 
current_savings = 0 #Needs to be reinitialized every 36  
starting_salary = float (input("Enter your salary: ")) 
guess = (high + low)/2
#iteration 

#while abs(current_savings-down_payment) > epsilon: make it if 
for guess0 in range (10001):
    #print(" ")
    #print("Beginning of guess0 loop")#our range is 0 to 10000
    #print('Steps Counter:', step_counter)
    salary = starting_salary #salary changes for many iterations. Need to be starting salary
    #print("Salary", salary)
    monthly_savings = (salary/12)*float((guess/10000))#Needs to be reinitialized every 36
    #print("Monthly Savings," , monthly_savings)
    percent_saved = guess/10000 #percent saved, reinitialized at the end of loop.
    #print("Guess:", guess)
    #print("Percent saved", percent_saved)
    while months < 36:
        
        months+=1 
        current_savings += monthly_savings 
        if months%6 == 0: 
            salary += (salary*semi_ann_raise)
            monthly_savings = ((salary/12)*percent_saved)
    #print("Loop done,current_savings:", current_savings)
    #print(" ")
    #print("down_payment, current_savings:", down_payment, current_savings)
    
    if current_savings > down_payment:
        high = guess
    
        #print("New high:", high)

        #current savings is too large
        
    elif current_savings < down_payment: 
       #if difference between the two is larger  
       low = guess 
       #print("New low:", low)
        
        
    if abs(current_savings-down_payment) <= epsilon:
        print("condition met, percent_saved:", percent_saved)
        print("Steps in bisection search:", step_counter)
        print("Current_savings:", current_savings)
        break
    
    if step_counter == 10000:
        print("It's not possible to save the amount in three years.")
        
    guess = (high+low)//2 
    #print("New guess:", guess)

    percent_saved = guess/10000
    #print("new percent saved:", percent_saved)
    months= 0
    current_savings = 0 
    salary = starting_salary
    step_counter+=1 

    



       