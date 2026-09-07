#!/usr/bin/python

import os, sys

## ----- Program will take input from the user and indicate whether the input is 
## a palindrome or not ------

result = raw_input("Please type a text string: ") #use raw_input in Python 2.7
reversed=''.join(reversed(result))

if (result == reversed):
    print ("Palindrome!") 
else:
    print("Not a Palindrome") 
