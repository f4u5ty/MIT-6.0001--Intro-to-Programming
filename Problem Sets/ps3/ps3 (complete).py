# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Luis Echevarria

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
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


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#my own function, getSum 
def getSum(word, valueDict): 
    """
    Assumes that word is a string, can be mixed, capitals and lower case. Assumes dictionary for Value Dict.
    returns the total value of the word. 
    
    """
    
    total = 0 
    word = word.lower()
    for i in word:
       #print("i: ", i)
        total += valueDict[i]
    #print("total points for word: ", total)
    return total 

#getSum(word, SCRABBLE_LETTER_VALUES)




#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    first_comp = getSum(word, SCRABBLE_LETTER_VALUES)
    if 1 > (7*len(word) - (3*(n-len(word)))): 
        secnd_comp = 1 
    else: 
        secnd_comp = (7*len(word) - (3*(n-len(word))))
    product = first_comp*secnd_comp
    return product 

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    
    """
    print()
    print("Current Hand: ", end = " ")
    for letter in hand.keys():
        #print("Current hand: ")
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(HAND_SIZE):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(HAND_SIZE / 4)) #with n being seven, evaluates to 3. 2.33, rounds up. 
    #what n is divided by, has no changed from 3 to 4. So, as to give out less vowels. 

    for i in range(num_vowels): #this seems to add vowels to hand. 
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = 1 
    
    for i in range(num_vowels, HAND_SIZE): #this seems to add consonants.   
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    
    PENALTIES: For a guess that is invalid: 
        either because it is 1. Not a real word.
                            2. The letters are not in the hand. 
    """
    word = word.lower() #need to lowercase words 
    new_hand = hand.copy() #new_hand is a copy 
    
    for i in word: #iterates over hand 
        if i in new_hand: #checks to see if character in the word 
            new_hand[i] -=1
            if new_hand[i] < 0: 
                new_hand[i] = 0
                #new_hand.pop(i)
            
        else: 
            continue
    
    return (new_hand)
#
# Problem #3: Test word validity
#
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
                #continue
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
    
    
    

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    new_hand = hand.copy()
    for i in hand: 
        if new_hand[i] == 0: 
            new_hand.pop(i)
    
    #print(handlen)
    return len(new_hand)


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0 
    while calculate_handlen(hand) != 0:
            
           display_hand(hand)
           word = input("Enter word, or '!!' to indicate that you are finished: ")
           
           if word == '!!': 
               print()
               print("Total score for this hand: ", total_score)
               print("- - - - - - - - - - - - - - - - - - - - - -")
               return total_score
               
           
           if is_valid_word(word, hand, word_list):
               total_score += get_word_score(word, calculate_handlen(hand))
               #print("Size of hand: ", str(calculate_handlen(hand)))
               print()
               print(word+" earned you " +str(get_word_score(word, calculate_handlen(hand)))+" points. Total score: " +str(total_score))
               hand = update_hand(hand, word)
        
           else:
               print()
               print("That is not a valid word, please choose another word.")
               hand = update_hand(hand, word)
        
         
    print()
    print("Ran out of letters.Total score this hand:", total_score)
    print("- - - - - - - - - - - - - - - - - - - - - - ")
    return (total_score)
               
               
#word_list = load_words()             
#hand = {'a':1, 'c': 1, 'i': 1, 'f': 1, 'x':1, 't': 1, "*":1}

#total = play_hand(hand, word_list)
#print(total)


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    #check to see if letter is in hand.
    new_hand = {}
    if letter not in hand: 
        print("That letter is not in your hand.")
        return hand 
    i = 0
    while i != 1:
        #print("inside while loop")
        new_letter = random.choice(VOWELS+CONSONANTS)
        #print("New Letter: ", new_letter)
        if new_letter in hand:
            #print("New_letter was in hand: ", new_letter)
            continue
        else:
            #print("New hand being created.")
            new_hand = hand.copy()
            #print("Value assigned, new letter:" + new_letter)
            new_hand[new_letter] = hand[letter]
            #print("Value assigned, entry recorded: ", str(new_hand[new_letter]))
            new_hand.pop(letter)
            #print("popped old shit.")
        i = 1
    #print(new_hand)
    return new_hand 

#hand = {'b':1, "r":1, 'i': 2, 'n': 1, 'a':3, '*':1}
#letter = 'a'
#substitute = substitute_hand(hand, letter)
#print(substitute)
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    hand_score = 0 
    series_score = 0 
    print()
    print("Reminder: Wildcards(*) only work for VOWELS")
    hands = int(input("How many hands would you like to play: "))
    i = 0
    while i < (hands):
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        user_answer= input("Would you like to substitute a letter (Enter yes or no)? ")
        user_answer = user_answer.lower()
        
        if user_answer == 'yes':
            letter = input("Choose a letter in your hand: ")
            hand = substitute_hand(hand, letter)
        
            
        hand_score = play_hand(hand, word_list) #this is the last total_score
        #print(hand_score)
        
        replay = input("Would you like to replay hand(enter yes or no)? ")
        replay = replay.lower() #we only handle lowercase words
        
        if replay == "yes":

            replay_score = play_hand(hand, word_list) #play a new hand. 
            #print("Replay Score: ", replay_score)
            #print("Hand Score: ", hand_score)
            if hand_score > replay_score:
                #print("first if statement, HS: ", hand_score)
                series_score+= hand_score
            else:
                #print("First else statement, RPS: ", replay_score)
        
                series_score+=replay_score
            
        else:
            #print("hand_score added to series score: ", hand_score)
            series_score += hand_score

        i+=1 
        
    print("Series Score(Total Score over all hands): ", series_score)
    
    
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
