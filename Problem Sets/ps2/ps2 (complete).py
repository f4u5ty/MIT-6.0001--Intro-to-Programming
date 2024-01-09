# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 00:59:23 2022

@author: Luis Echevarria
"""

WORDS_LIST_FILENAME = "words.txt"


import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


#wordlist = load_words()
#secret_word = choose_word(wordlist), first word chosen was centroids. 
#secret_word = "centroids"
#print("Secret Word:", secret_word)
#letters_guessed = "zbenwrlkoiys"
#letters_guessed = list(letters_guessed)

#function is complete 
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    i2=0 
    i=0
    while i < len(letters_guessed):
        if letters_guessed[i] in secret_word:
            #print("hit")
            i2 +=1 
        if i2 == (len(secret_word)-1):
            #print("True")
            return True
        #print("i:", i)
        i+=1 
    return False
          
#print ("Word Contained in guesses:", is_word_guessed(secret_word, letters_guessed))
#game_won = is_word_guessed(secret_word, letters_guessed)
#print("Game Won?:", game_won)


#complete function 
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
      
    '''
    guessed_letters = ["_"]* len(secret_word)
    i = 0 
    i2 = 0 
    while i <  len(letters_guessed):
            i2 = 0 
            while i2 < len(secret_word):
                if letters_guessed[i]== secret_word[i2]: #i2 is going to be position of letter in word.
                    #pop
                    guessed_letters.insert(i2, letters_guessed[i]) #insert
                    guessed_letters.pop(i2+1) #remove the underscore
                i2+=1 #I think we have to delete items before we can add to that position. .pop method
            i+=1
    return (''.join(guessed_letters))
                
    
#guessed_letters = get_guessed_word(secret_word, letters_guessed)
#print("Guessed Word:", str(guessed_letters)) 



    # FILL IN YOUR CODE HERE AND DELETE "pass"
   
    #function complete
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lower_case = list(string.ascii_lowercase)
    #print(lower_case)
    i = 0 
    while i < len(letters_guessed):
        if letters_guessed[i] in lower_case: 
            lower_case.remove(letters_guessed[i])
        i+=1 
    return ("".join(lower_case))

#available_letters = get_available_letters(letters_guessed)
#print("Available Letters:", available_letters) 
 

#word_list = load_words()

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #consonants = "bcdfghjklmnpqrstuvwxyz"
    upper_word = secret_word.upper()
    vowels = "aeiouAEIOU"
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    all_letters = upper_case + lower_case 
    warning = 0 
    guess = 0 
    letters_guessed = []
    length_word = len(secret_word)
    print(" ")
    print("Welcome to the Gallows!")
    print(" ")
    print("I am thinking of a word that is "+str(length_word)+" letters long.")
    print("_ _ _ _ _ _ _ _ _ ")
    print("You have 6 guesses left.")
    print("You have 3 warnings left.")
    print("Available Letters: ", lower_case)
    #print("All_Letters: ", all_letters)
    
    while guess < 6: 
        
        error_check = 0 
        
        while error_check != 1:
            
            if guess >= 7:
                print("You have run out of guesses.")
                return False
            
            letter = input("Please guess a letter: ")
            
            if letter == "*": 
                print("Possible Words are: ",show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                continue
                
            
            if letter in upper_case: 
                letter = letter.lower()
            
            if guess >= 7: #checking for end result inside error check. 
                print("You have run out of guesses.")#in case of stubborn individual.
                print("The secret Word is: ", secret_word)
                return False
            
            if ((letter not in secret_word) and (letter in vowels)): #checks for vowels that are not in word. 
                print("Vowel, not in secret word. 2 Guesses used.")
                guess+=2
                
            elif (letter not in all_letters) or (letter in letters_guessed): #checks for symbols or duplicates. 
                
                if (letter in letters_guessed):
                    #When there is a duplicate letter. 
                    print("This letter has already been guessed: ",get_guessed_word(secret_word, letters_guessed))
                    if warning < 3: #Warns the user if they have any warnings left. 
                        warning+=1 
                        print("Warning left: ", (3-warning))
                    
                    else: #removes guesses if they are out of warnings. 
                        guess+=1 
                        print("Guesses left: ", (6-guess))
                #catches symbols and warns the user about entering things that are not letters. 
                elif warning < 3:
                    warning+=1
                    print("Oops! That is not a valid letter. You have " + str(3-warning)+" warnings left:", get_guessed_word(secret_word, letters_guessed))
                    print("You have "+ str(3-warning)+ " warnings left.")
                    
                #this is if warnings have been all used up. 
                elif (warning >= 3):
                    guess+=1 
                    print("You have lost a guess. Guesses left:", str(6-guess))
                    #checks to see if game should end. 
                    
               
                if ((letter in letters_guessed) and (letter not in all_letters)): 
                    letters_guessed.remove(letter)    
                    
            else: 
                error_check +=1
                #exits the error check if guess has passed all conditions. 
        #Error check here is reset.
        if guess == 5: #here we check for guess being higher than the limit, outside the error check
            print("You have run out of guesses.")
            print("The secret word is: ", secret_word)
            return False 
        error_check = 0   
        letters_guessed.append(letter.lower())#final letter finally appended to list. 
        #print("Letters_guess: ", letters_guessed)
        
        if (letter in secret_word) or (letter in upper_word) : #checks to see if letter is in secret word. 
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            print("_ _ _ _ _ _ _ _ _ ")
            print(" ")
            print("Guesses left: ", (6-guess))
            print("Available letters: ", get_available_letters(letters_guessed))
            #This is the win condition. (Working)
            if (get_guessed_word(secret_word, letters_guessed)==secret_word): 
                #print("Letters_guessed: ", letters_guessed)
                print("")
                print("Congrats, you have defeated the Hangman and escaped the Gallows.")
                print("Total Score: " + str((6-guess)*len(letters_guessed)))
                return True 
        
        else:
            if guess == 5: #we check for guess here so it never goes overboard. a
            
                print("You have run out of guesses!")
                print("The secret word is: ". secret_word)
                return False 
            guess+=1
            print(" ")
            print("Oops, sorry, that letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            print("_ _ _ _ _ _ _ _ _ ")
            print(" ")
            print("Guesses left: ", (6-guess))
            
            
            





def match_with_gaps(my_word, other_word):
    
    if len(my_word) == len(other_word): 
        i = 0 
        while i < len(my_word): 
            #print("in loop, i is: ", i), used to get rid of infinite loop. 
            if my_word[i] != "_": #checking to see if there is a letter. 
                
                if my_word[i] == other_word[i]:
                    i+=1 #continues the check
            
                else:
                    #print("False") #Check has failed, exits program and returns False. 
                    return False
                
            elif other_word[i] in my_word:
                #print("False") #Checks to see if the letter occurs elsewhere in the string. 
                return False
            
            else:
                i+=1
    else: #If they are not the same length. Return False. 
        #print("False")
        return False
                
    #print("True")#if while loop ends with no exit tripped. Returns True. 
    return True 

#match_with_gaps(my_word, other_word)


"""
Show all possible matches. Single parameter. 
"""


def show_possible_matches(my_word):
    i = 0 
    possible_list = []
    words_list = load_words()
    check =  match_with_gaps(my_word, words_list[i])
    
    while i < len(words_list):
        check =  match_with_gaps(my_word, words_list[i])
        #print ("check", check)
        if check:
            #print("Inside if statement")
            possible_list.append(words_list[i])
        i+=1 

    return ", ".join(possible_list)
        
#print(show_possible_matches(my_word))
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

"""
Hangman with Hints
""" 


#my_word = "te_t"
#other_word = "tact"#, this example returned False.

#my_word = "a__le"
#other_word = "apple" #, now this is printing True. 

#my_word = "a_ple" #, correctly returns False now. 
#other_word = "apple"

#my_word = "a__le"
#other_word = "banana", prints False. 
    
#we need to figure out how to get the things we need. 
