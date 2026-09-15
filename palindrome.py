#!/usr/bin/python

import os, sys

## ----- Program will take input from the user and indicate whether the input is 
## a palindrome or not ------

result = input("Please type a text string: ")
reversed=''.join(reversed(result))

if (result == reversed):
    print ("Palindrome!") 
else:
    print("Not a Palindrome") 
