# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:51:52 2022

@author: f4u5t
"""

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

text = get_story_string()
words = load_words(WORDLIST_FILENAME)
shift = 4 
#print(words)

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        self.message_text = text 
        self.valid_words = list()

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
            

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
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
           
        return letters
    
    
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        message = self.get_message_text()
        lower = string.ascii_lowercase
        letters = self.build_shift_dict(shift)
        i = 0
        keys = list(letters.keys())
        new_message = str()
        while i < len(message):
           value = letters.get(message[i])
           #print("value:", value)
           if message[i] in letters:
               #print("message[i] in letters") 
               if message[i] in lower:
                   #print("message[i] in lower")
                   if (shift+value) > 25:
                       #print("Shift+value: ", shift+value)
                       new_message+=keys[shift]
                       #print("new_message+=keys[shift]")
                       #print("keys[shift]", keys[shift])
                       i+=1
                   
                   else:
                       #print("else: new_message+=keys[value+shift]")
                       new_message+=keys[value+shift]
                       i+=1
               
               elif (value+shift) > 51:
                   #print("value+shift")
                   value = letters.get(message[i]) 
                   new_message+=keys[(value-26)+shift]
                   i+=1
               else: 
                   new_message+=keys[(value+shift)]
                   i+=1 
               
           else: 
               new_message += message[i]
               i+=1
               
        #print(new_message)
        return new_message
    
    
message = Message(text)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text = text 
        self.valid_words = load_words(words)
        self.shift = int()
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
       
plainMessage = PlaintextMessage(text, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(words_list)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        i= 0 
        best_shift = 25-i 
        new_word_count = 0 
        word_count = 0 
        word_list = list(CiphertextMessage.get_valid_words(self))
        while i < 26: 
            decrypted_text = CiphertextMessage.apply_shift()
            split_text = decrypted_text.split()
            i2 = 0 
            while i2 < len(split_text):
                #iterates over length of encrypted words
                if is_word(word_list, split_text[i2]): 
                    new_word_count+=1
                i2+=1 
                #compares against diffferent decrypted strings
            
            i2 = 0 
            if word_count>new_word_count:
                new_word_count= 0
            else: 
                word_count = new_word_count
                best_shift = 25-i
                new_word_count = 0
        i+=1 
        decrypted_text = CiphertextMessage.apply_shift(CiphertextMessage, best_shift)
        result = (best_shift,decrypted_text)    

        return result
        



#cipher_message = CiphertextMessage(message)
#print(cipher_message.decrypt_message())

words = load_words('words.txt')
print(words)