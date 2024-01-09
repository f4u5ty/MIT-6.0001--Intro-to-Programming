# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:19:23 2022

@author: f4u5t
"""

def hangman(secret_word):
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
    consonants = "bcdfghjklmnpqrstuvwxyz"
    vowels = "aeiou"
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
            
            letter = input("Please guess a letter: ")
            
            if ((letter not in secret_word) and (letter in vowels)):
                print("Vowel, not in secret word. ")
                guess+=2
                
            elif (letter not in all_letters) or (letter in letters_guessed):
                
                if (letter in letters_guessed):
                    
                    print("This letter has already been guessed: ",get_guessed_word(secret_word, letters_guessed))
                    if warning < 3: 
                        warning+=1 
                        print("Warning left: ", (3-warning))
                    
                    else: 
                        guess+=1 
                        print("Guesses left: ", (6-guess))
                
                elif warning < 3:
                    warning+=1
                    print("Oops! That is not a valid letter. You have " + str(3-warning)+" warnings left:", get_guessed_word(secret_word, letters_guessed))
                    print("You have "+ str(3-warning)+ " warnings left.")
                    
            
                elif (warning >= 3):
                    guess+=1 
                    print("You have lost a guess. Guesses left:", str(6-guess))
                    if guess > 6: 
                        return False
               
                if ((letter in letters_guessed) and (letter not in all_letters)): 
                    letters_guessed.remove(letter)
                    
            else: 
                error_check +=1
                
        letter = letter.lower()
        error_check = 0   
        letters_guessed.append(letter)
        #print("Letters_guess: ", letters_guessed)
        
        if letter in secret_word:
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            print("_ _ _ _ _ _ _ _ _ ")
            print(" ")
            print("Guesses left: ", (6-guess))
            print("Available letters: ", get_available_letters(letters_guessed))
            
            if (get_guessed_word(secret_word, letters_guessed)==secret_word): 
                print("")
                print("Congrats, you have defeated the Hangman and escaped the Gallows.")
                return True 
        
        else: 
            guess+=1
            print(" ")
            print("Oops, sorry, that letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            print("_ _ _ _ _ _ _ _ _ ")
            print(" ")
            print("Guesses left: ", (6-guess))
            
            
            

  
hangman(secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)