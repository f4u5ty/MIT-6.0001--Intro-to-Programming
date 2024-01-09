# -*- coding: utf-8 -*-
"""
Created on Tue May  3 01:42:14 2022

@author: f4u5t
"""
import string 
lowerCase = string.ascii_lowercase
upperCase = lowerCase.upper()
#print(lowerCase)
#print(upperCase)
alephBet = lowerCase + upperCase
letters = dict() 
#print(alephBet)
i = 0
while i < len(alephBet): 
   letters[alephBet[i]] = i 
   i+=1
print(letters)

while True: 
    try: 
        
        
        
        
        
        
        
        
    except IndexError: 
        print("try a number between 1 and 26")













lowerCase = string.ascii_lowercase
upperCase = lowerCase.upper()
#print(lowerCase)
#print(upperCase)
alephBet = lowerCase + upperCase
letters = dict() 
#print(alephBet)
i = 0
while i < len(alephBet): 
   letters[alephBet[i]] = i 
   i+=1
   
shift_dict = dict()
i = 0
letter_keys = list(letters.keys())
while i < len(letter_keys): 
       if letter_keys[i] in lowerCase:
           if i+shift > 25: 
               shift_dict.update({letter_keys[i]:letter_keys[(shift+i)-26]})
               #here we want to shift value of lowerCase letters
               #i+=1 
           else:
               #print("shift+i", shift+i)
               #print('letter_keys[shift+i]', letter_keys[shift+i])
               shift_dict.update({letter_keys[i]: letter_keys[shift+i]})
           i+=1 
               
           
            
       elif letter_keys[i] in upperCase: 
           if i + shift > 51: 
               shift_dict.update({letter_keys[i]:letter_keys[(i-26)+shift]})
               #i+=1 
           else: 
               shift_dict.update({letter_keys[i]:letter_keys[i+shift]})
               #i+=1
        
           i+=1
           
       else: 
           i+=1
#this currently works, just can't get it to return shift_dict 
#print(shift_dict)           
return shift_dict