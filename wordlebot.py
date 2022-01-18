# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 08:26:47 2022

@author: ninja_of_physics
"""

import re
from collections import OrderedDict
    
def CommonLetters(words):
    for w in words:
        break
# Trim the word list based on the results from a guess. 
def TrimWords(color_dict, words):
    charIndex = 0
    for c in color_dict:
        new_words = []
        if color_dict[c] == 'y':
            for w in words:
                if w[charIndex] != c and c in w:
                    new_words.append(w)
            words = new_words
        elif color_dict[c] == 'b':
            for w in words:
                if c not in w:
                    new_words.append(w)
            words = new_words
        elif color_dict[c] == 'g':
            for w in words:
                if w[charIndex] == c:
                    new_words.append(w)
            words = new_words
        charIndex += 1
    return words            
                    

# Function that handels the color results 
def CheckGuess(guess, words):
    color_dict = OrderedDict()
    for c in guess:
        cg = input("{} color (green, yellow, black): ".format(c))
        cg = cg.lower()[0]
        color_dict[c] = cg
    print(color_dict)
    words = TrimWords(color_dict, words)
    return words
        
if __name__ == "__main__":
    # Make a list of all 5 letter words
    words = []
    with open("words.txt", 'r') as file:
        for line in file:
            line = line.strip('\n').lower()
            if '\'' in line or '-' in line or '.' in line:
                continue
            if len(line) == 5:
                print(line)
                words.append(line)
    
    guessCount = 0
    guess = input("What's your first guess: ")
    
    # After the first guess is given, ask about the results of the word. 
    while guessCount < 5:
        guessCount += 1
        words = CheckGuess(guess, words)
        print("After your {} guess there are {} possible words".format(guessCount, len(words)))
        print(words)
        guess = input("What is your next guess: ")
   

