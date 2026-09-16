## This script is for practicing Python coding
## Use python -V to get version. My version is 3

# One line comment
# """" are used for multi line comments """"

import os, sys

## ------- Testing Strings ----------------

a = "string"
b = "STRING"
print("This prints tr: " + a[1:3])  # prints 'tr'
print("This prints string: " + a[:-1])  # prints 'strin' (calculates from end to beginning because of -)
print (a.count('r'))  # counts number of r's
print (a.find('r'))  # prints location of r in the string (starting a 0)
print ("This prints the string in lowercase: " + (b.lower()))  # prints string in lowercase
print ("This prints the string in uppercase: " + (a.upper()))  # prints string in upper case
print ("This replaces one character with another: " + (a.replace('r','z')))  # replaces one character with another and prints result
print ("This removes a specified character from the string: " + (a.strip('g')))  # removes specified character from string and prints result