# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 02:34:27 2022

@author: f4u5t
"""



sequence = 'abc'
def get_permutations(sequence): 
    if len(sequence) == 1: 
            return [sequence]
    """
    if sequence is a single character. There is only way one to order it.
    returns a singleton list.
    """
    """
    suppose we have a list of all permutations but the first character.
    """
    perms = get_permutations(sequence[1:])
    
    
    """
    this is our list of permutations with all but the first character. 
    now we have to insert the first character of sequence into every position for every permutation. 
    so, here we would need the length of each string.
    """
    char = sequence[0]
    """
    We need to iterate over the perms, and the iterate over the strings in perms and add the character, 
    then save the result to a list. 
    """ 
    result = []
    
    i = 0 
    while i < len(perms): #iteration over list
        i2 = 0 
        while i2 < len(perms[i])+1: #iteration over string. 
            result.append(perms[i][:i2]+char+perms[i][i2:])
            i2+=1
        i2 = 0 
        i+=1 
    
    return result 
            

print(get_permutations(sequence))
