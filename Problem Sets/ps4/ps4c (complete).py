# Problem Set 4C
# Name: Luis Echevarria 


import string
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #these need the init parent constructor. Go over this again before moving on
        #also delete these comments. 
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        permutation = vowels_permutation
        VOWELS_LOWER = 'aeiou'
        VOWELS_UPPER = 'AEIOU'
        permutation_upper = permutation.upper()
        permutation = permutation_upper + permutation 
        CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
        CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
        VOWELS = VOWELS_UPPER + VOWELS_LOWER
        CONSONANTS = CONSONANTS_UPPER + CONSONANTS_LOWER
        shift_dict = {}
        i = 0
        while i < len(VOWELS):
            shift_dict[VOWELS[i]] = permutation[i]
            #print('i:', i) 
            i+=1
             
        i = 0 
        while i < len(CONSONANTS): 
            shift_dict[CONSONANTS[i]] = CONSONANTS[i]
            i+=1 
             
        return shift_dict 
    

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        spec_chars = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""
        message = self.get_message_text()
        new_message = ""
        i = 0 
        while i < len(message):
            if message[i] in spec_chars: 
                new_message+=message[i]
            
            else:
                #print('i:', i)
                #print("new_message:", new_message)
                #print(transpose_dict)
                #print("transpose m[i]: ", transpose_dict.get(message[i]))
                new_message += transpose_dict.get(message[i])
            i+=1 
            
        #print(new_message )
        return new_message 
        
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text 

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        VOWELS_LOWER = 'aeiou'
        VOWELS_UPPER = 'AEIOU'
        VOWELS = VOWELS_UPPER+VOWELS_LOWER
        encrypted_message = self.message_text
        encrypted_message = encrypted_message.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        word_list = load_words(WORDLIST_FILENAME)
        vowel_permutation = "eaiuo"
        permutations = get_permutations(vowel_permutation)
        i = 0
        new_word_count = 0 
        word_count = 0 
        decrypted_word = str()
        split_message = encrypted_message.split(' ')
        best_message = str()
        correct_vowel = str()
        while i < len(permutations): #iterates over all permutations
            #print("while i < len(permutations)")
            #print("i: ", i )
            shift_dict = self.build_transpose_dict(permutations[i])
            keys = list(shift_dict.keys())
            values = list(shift_dict.values())
            #print("shift_dict: ", shift_dict)
            #print("permutations[i]: ", permutations[i])
            #builds a dictionary based on permutation in ith position
            #All we need to do, is build another transpose dictionary
             

            reverse_dict = dict()
            keys = list(shift_dict.keys())
            values = list(shift_dict.values())
            i2 = 0 
            while i2 < len(keys): 
                reverse_dict[values[i2]] = keys[i2]
                i2+=1 
            
            for word in split_message:
                #print("for word in split_message")
                #print("word: ", word)
                char = 0 
                while char < len(word):
                    #print("while char < len(word)")
                    #print("char: ", char)
                    if word[char] in VOWELS:
                        #print("if word[char] in VOWELS")
                        #print("word[char]: ", word[char])
                        #access the regular letter. The correct order.
                        #to try and create a real word. We would have access to the shifted one.
                        engine = 0 
                        while engine < len(keys):
                            #print("engine: ", engine)
                            #print("values[engine]:", values[engine])
                            if word[char] == values[engine]:
                                #print("word[engine]==values[engine]")
                                #print("word[char]:", word[char])
                                correct_vowel = keys[engine]
                                #print("correct_vowel:", correct_vowel)
                            engine+=1
                        engine = 0 
                        decrypted_word+= correct_vowel
                        
                    else: 
                        decrypted_word+=word[char]
                        
                    char+=1 
                
                if is_word(word_list, decrypted_word):
                    #print("if decrypted word in word list")
                    #print("decrypted_word: ", decrypted_word)
                    new_word_count+=1
                    
                if new_word_count > word_count:
                    best_message = self.apply_transpose(reverse_dict)
            
            best_message += " "
            decrypted_word = str()        
            i+=1
            
        return best_message 
        
                    
                
            
    

if __name__ == '__main__':

    # Example test case

    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print(enc_dict)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage("Have you heard the good news?")
    permuation = 'eaiuo'
    sub_dict = message.build_transpose_dict(permutation)
    print(sub_dict)
    print("Original: ", message.get_message_text(), 'permutation: ', permutation)
    print("Expected encryption: Heva yuo haerd tha guud naws?")
    print("Actual Encryption: ", message.apply_transpose(sub_dict))
    encrypted_message = EncryptedSubMessage(message.apply_transpose(sub_dict))
    print("Decrypted message: ", encrypted_message.decrypt_message())
    
    
    
    permutation = 'ouiea'
    text = 'Have you heard the good news?'       
    subMessage = SubMessage(text)
    transpose_dict = subMessage.build_transpose_dict(permutation)
    print("transpose_dict:", transpose_dict)
    print("Original Message:", text)
    print("Expected Encryption: Hovu yea huord thu geed nuws?")
    print("Actual Encryption: ", subMessage.apply_transpose(transpose_dict))
    encrypted_mess = EncryptedSubMessage(subMessage.apply_transpose(transpose_dict))
    print('Decrypted message: ', encrypted_mess.decrypt_message() )
    
