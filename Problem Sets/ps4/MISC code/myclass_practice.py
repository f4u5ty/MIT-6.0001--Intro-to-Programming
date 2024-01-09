# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:48:30 2022

@author: f4u5t
"""

'''
    Lets say I want to create a type Person and I want each instance of person have the attributes. 
   nature, sign  Need to create methods to get this information and also to be able to 
    set this information for each instance. 
'''

import string 

class Person(object): 
    #ATTRIBUTES, set them equal to the type you want them to be. 
    #init, is the initializing of a new object
    def _init_(self): 
        self.sign = str()
        self.name = str()
        self.age = int()
    #GETTER METHODS, these are class functions that retrieve information   
    def get_age(self): 
        return self.age
    def get_name(self): 
        return self.name
    def get_sign(self): 
        return self.sign
    #SETTER METHODS, these are class functons that set values to our attributes
    def set_age(self, age): 
        self.age = age  
    def set_name(self, newname): 
        self.name = newname
    def set_sign(self, newsign):
        self.sign = newsign
        

#Person.set_sign(Person, "Saggitarius")
#print(Person.get_sign(Person))

#This code here sets "Saggitarius" as a sign. 
#The next line prints that persons sign. 
#Creating a new instance

class Luis(Person):
    #all of Luis' special attributes
    def _init_(self): 
        self.nationality = str()
        
    def get_nationality(self): 
        return self.nationality
        
    def set_nationality(self, newnationality): 
        self.nationality = newnationality
        
        

#These are the inherited classes. From the super class. 
Luis.set_sign(Luis, "Saggitarious")
Luis.set_age(Luis, 27)
Luis.set_name(Luis, "Echevarria")

print(Luis.get_age(Luis))
#print(Luis.get_name(Luis))
#print(Luis.get_sign(Luis))

#This is the method that only Luis object has. 
Luis.set_nationality(Luis, "Mexican-American")
#print(Luis.get_nationality(Luis))




 
"""
message = "Have you heard the good news?"  

"""
def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

text = get_story_string()
#print( message_text) 

class Test_Class(object): 
    def _init_(self, text): 
        self.text
    
    def set_encrypted_text(self, newtext): 
        self.text = newtext
        
    
    def get_encrypted_text(self): 
        return self.text 
    
Test_Class.set_encrypted_text(Test_Class, text)
print(Test_Class.get_encrypted_text(Test_Class))

    
