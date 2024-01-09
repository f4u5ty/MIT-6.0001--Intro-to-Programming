# Problem Set 4B
# Name: Luis Echevarria


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
        self.valid_words = load_words(WORDLIST_FILENAME)

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
        while True: 
            try:
                
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

            except IndexError: 
                print("try a number between 1 and 26")
                return None

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
        while True: 
            try: 
                lowerCase = string.ascii_lowercase
                upperCase = lowerCase.upper()
                alephBet = lowerCase + upperCase
                message_text = self.get_message_text()
        
                shift_dict = self.build_shift_dict(shift)
                new_message = str()
                i=0 
                while i < len(message_text): 
                    #print("inside first loop")
                    if message_text[i]in alephBet: 
                    #print("Inside first if statement")
                        new_message+=shift_dict[message_text[i]]
                
                    else:
                        #print("else")
                        new_message+=message_text[i]
                        #print("i:", i)
                    i+=1
                    #currently works just can't get it to return message 
                    #print(new_message)
                return new_message 
            except TypeError: 
                return ''
        


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
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift 
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

    def change_shift(self, newshift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = newshift
        

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
        self.valid_words = load_words(WORDLIST_FILENAME)

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
        twenty_six = 26 
        word_count = 0 
        new_word_count = 0 
        words = self.valid_words
        i = 0
        while i < 26:
            #print("While i < 26:")
            decrypted_message = self.apply_shift(twenty_six-i)
            split_message = decrypted_message.split()
            i2 = 0 
            while i2 < len(split_message):
                #print("While i2 < len(split_message):")
                if is_word(words, split_message[i2]):
                    #print("if is_words():")
                    new_word_count +=1 
                i2+=1 
            
            i2 = 0 
            if word_count>new_word_count:
                #print("if word_count>new_word_count:")
                new_word_count= 0
                
            else:
                #print("else:")
                best_text = decrypted_message
                word_count = new_word_count
                best_shift = 26-i
                new_word_count = 0
            i+=1
        result = (best_shift, best_text )
        #print("result: ", result)
        return result
    
    


#if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    
    ####Testing of every method for message object####
    
#   message = Message(text)
#   #Intialization of the class
#
#    message_text = message.get_message_text()
#    print("Expected Output: Have you heard the good news?")
#    print("Actual Output: ",message_text) 
#    #testing of get_message_text method 
#
#    #valid_words= message.get_valid_words()
#    #print(valid_words) #DONE, prints 55k words
#    #testing of get_valid_words() method 
#
#    shift_dict = message.build_shift_dict(24)
#    print(shift_dict)
#    #testing of build_shift_dict(shift) method. 
#    #NOTES: throws an index error if shift is larger than 26. 
#    #not sure if professor wants this issue addressed or it is understood 
#    #by users not to input more than 26 because it is redundant. 
#    #DONE: Errors handled
#    
#    
#    encrypted_message = message.apply_shift(24)
#    print("Expected Output: Fytc wms fcypb rfc emmb lcuq?")
#    print("Actual Output:", encrypted_message)
#    #testing of apply_shift() method 
#    #NOTES: This method relies on another method, build shift. 
#    #this means this method is also restricted from using a value more than 26 
#    #for shift.
#    #DONE: Errors handled
    
#    ####Testing of message object, complete#### 
     
     
#    ####Testing of the PlaintextMessage object####
#    plain_message = PlaintextMessage(text, 24)
#    ###initialization of class

#    shift1 = plain_message.get_shift()
#    print("Expected shift1: 24")
#    print("Actual shift1: ", shift1)
#    #DONE, returns shift 

#     print("Expected encryption_dict: {'a': 'y', 'b': 'z', 'c': 'a', 'd': 'b', 'e': 'c', 'f': 'd', 'g': 'e', 'h': 'f', 'i': 'g', 'j': 'h', 'k': 'i', 'l': 'j', 'm': 'k', 'n': 'l', 'o': 'm', 'p': 'n', 'q': 'o', 'r': 'p', 's': 'q', 't': 'r', 'u': 's', 'v': 't', 'w': 'u', 'x': 'v', 'y': 'w', 'z': 'x', 'A': 'Y', 'B': 'Z', 'C': 'A', 'D': 'B', 'E': 'C', 'F': 'D', 'G': 'E', 'H': 'F', 'I': 'G', 'J': 'H', 'K': 'I', 'L': 'J', 'M': 'K', 'N': 'L', 'O': 'M', 'P': 'N', 'Q': 'O', 'R': 'P', 'S': 'Q', 'T': 'R', 'U': 'S', 'V': 'T', 'W': 'U', 'X': 'V', 'Y': 'W', 'Z': 'X'} ")
#     print("Actual encryption_dict", encryption_dict)
#     #DONE, gets encryption_dict 

#     encrypted_message = plain_message.get_message_text_encrypted()
#     print("Expected encrypted_message: Fytc wms fcypb rfc emmb lcuq?")
#     print('Actual encrypted_messsage:', encrypted_message)
#     #DONE, gets encrytped message. 

#     plain_message.change_shift(20)
#     #CHANGE SHIFT, THEN GET SHIFT
#     shift1 = plain_message.get_shift()
#     #SET SHIFT1 equal to the new shift 
#     print("Expected shift1: 20")
#     print("Actual shift1: ", shift1)
#     ###Testing Complete###
    
#     ## Testing of Cypher_message ##
#     #encrypted_text = "Fytc wms fcypb rfc emmb lcuq?"
#     #cipher_message = CiphertextMessage(encrypted_text)
#     #decrypted_text = cipher_message.decrypt_message()
#     #print("Expected Output: Have you heard the good news?")
#     #print("Actual Output: ", decrypted_text[1])
#     #print("Tuple of best value/unencrypted_message")
    
#     story = get_story_string()
#     cipher_message = CiphertextMessage(story)
#     decrypted_text = cipher_message.decrypt_message()
#     print("Decrypted message and best shift value: ")
#     print(decrypted_text)
    
    
    
    
    
