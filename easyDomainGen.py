# EasyDomainGen.py
# -------
# @ianmcshane 2019
# -------
# This will generate an easy to speak domain name, in English,
# comprised of two three letter words.
# MUST not start with a vowel.
# MUST not end with a vowel.
# MUST not contain Q (hard to pronounce)
# MUST not contain O or ZERO (avoid confusion)
# MUST not contain L (avoid confusion)

# Create a list of the alphabet characters - alphabet - 
# we can use that to loop through in each iteration

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z"]

# Create a list of vowels

vowels = ["a", "e", "i", "o", "u"]

# Create a list of unwanted letters

unwanted = ['q', 'o', 'l']

# Create a list of strings - tlds - which hold the list 
# of TLDs we want to use

tlds = [".com", ".net"]

# Create a list of strings - twoChars - which will hold the first
# set of characters
twoChars = []

# Create a list of strings - threeChars - which will hold the final
# three letter words

threeChars = []

# Check the alphabet is created correctly
print('The Alphabet contains ' + str(len(alphabet)) + ' letters, OK?')

# FIRST PASS - create list with two letters
# 
# Loop through alphabet (for each item in alphabet)
# adding the two chars to a list

for letter in alphabet:
   # check for unwanted letters
   if letter in unwanted:
      continue
   if letter in vowels:
      continue # I don't want it to start with a vowel
   currentLetter = letter
   for nextLetter in alphabet:
      if nextLetter in unwanted:
         continue
      twoChars.append(currentLetter + nextLetter)

# SECOND PASS - create the list with three letters
# Loop through twoChars, creating a new string with each letter

for word in twoChars:
   for letter in alphabet:
      if letter in unwanted:
         continue
      threeChars.append(word + letter)

print('There are ' + str(len(twoChars)) + ' combinations of two chars.') # should be 676

print('There are ' + str(len(threeChars)) + ' combinations of three chars.') # should be 17576


