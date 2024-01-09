# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:40:00 2022

@author: f4u5t
"""


VOWELS = 'aeiou*'
import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

#word_list = load_words()
#word = "c*ws"
#hand = {'c': 1, 'o': 1, "w": 1, 's': 1, '*': 1, 'b': 1}

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word = word.lower()
    new_hand = hand.copy()
    position = word.find("*") #position of asterisk 
    
    if position >= 0: #if an asterisk was found. 
        #print("Asterisk was found in word.")    
        for i in VOWELS:
            #print("iterating over VOWELS: ", i)
            word = list(word)
            #print("Word turned into list: ", str(word))
            word[position] = i 
            word = "".join(word)
            #print("Joins word into string: ", word)
            #print("Is word in word_list?")
            if word in word_list: #checks to see if word is in wordlist
            #print("word is in list? Yes.")
                return True
            #else: 
                #False
                #print("Word is in list? No.")   
    
    if word in word_list: 
        for i in word: 
            if i in new_hand: 
                new_hand[i] -= 1
                if new_hand[i] < 0: 
                    return False
            else: 
                return False 
        return True 

word_list = load_words()
#word = "qu*b"
#hand = {"q":, "*":1, "e": 1, "u":1, "p":1, "m":1, 'b'}
#test = is_valid_word(word, hand, word_list)
#print(test)


