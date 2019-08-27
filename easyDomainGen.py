#! /usr/bin/env python3

# EasyDomainGen.py - @ianmcshane - August 2019
# -------
# REQUIRES: pyEnchant (pip install pyEnchant)
#
# This will return a random, easy to speak domain name, in English,
# comprised of two three letter words.  
# To ensure it is easy to speak, the middle letter is always a vowel.
# We'll use pyEnchant to check the words exist in English before 
# creating the domain names.

import sys
import random
import enchant

# Set up the dictionary for pyEnchant
dictionary = enchant.Dict("en_US")

# Create a list of the alphabet characters - alphabet - 
# we can use that to loop through in each iteration

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z"]

# Create a list of vowels

vowels = ["a", "e", "i", "o", "u"]

# Create a list of unwanted letters

unwantedSounds = ['sh', 'ph']
unwantedLetters = ['q', 'o', 'l']

# Create a list of strings - tlds - which hold the list 
# of TLDs we want to use

tlds = [".com"]

# Create a list of strings - threeChars - which will hold the final
# three letter words
words = []

# Create the list for the generated domain names

domains = []

# Create the three letter words
for letter in alphabet:
   # if letter in vowels:
   #   continue # I don't want it to start with a vowel
   currentLetter = letter
   for nextLetter in alphabet:
      if nextLetter in vowels: # vowel in the middle
         for lastLetter in alphabet:
           # if lastLetter in vowels:
            #   continue # no vowel at the end, please
            thisWord = (currentLetter + nextLetter + lastLetter)
            if dictionary.check(thisWord):
               words.append(thisWord)

# Create all of the two-word permutations
# Word 2 must not start with the same letter as word 1, and 
# the domain should not appear to be one word.

for tld in tlds:
    for word in words:
        for nextword in words:
            if word == nextword:
                continue
            if word[2] == nextword[0]:
                continue
            if word[2] + nextword[0] in unwantedSounds:
                continue
            domains.append(word + nextword + tld)

def getRandomDomain():    
    randomNumber = random.randint(0, len(domains))
    randomDomain = domains[randomNumber]
    return randomDomain

def getAllDomains():
    return domains

def getMultipleRandomDomains(count):
    domainList = []
    for x in range(count):
        domainList.append(getRandomDomain())
    return domainList

if 'easyDomainGen.py' in sys.argv[0]:
    # if script is running from a shell
    # but with no arguments, print one random domain
    print('- easyDomainGen.py -')
    print('Pulling a random domain from ' + str(len(domains)) + ' domains.')
    print('---')
    print(getRandomDomain())
