# EasyDomainGen.py
# -------
# @ianmcshane 2019
# -------
# This will generate an easy to speak domain name, in English,
# comprised of two three letter words.


# Create a list of the alphabet characters - alphabet - 
# we can use that to loop through in each iteration

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z"]

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
   currentLetter = letter
   for nextLetter in alphabet:
      twoChars.append(currentLetter + nextLetter)

# SECOND PASS - create the list with three letters
# Loop through twoChars, creating a new string with each letter

for word in twoChars:
   for letter in alphabet:
      threeChars.append(word + letter)

print('There are ' + str(len(twoChars)) + ' combinations of two chars.') # should be 676

print('There are ' + str(len(threeChars)) + ' combinations of three chars.') # should be 17576


