#!/usr/bin/python

import os, sys

## ----- Program asks user for a number and prints out a message
## ----- indicating if the number is odd or even ------

getNum = int(input("Please enter a number: "))

# If you divide a number by two and it gives a remainder of 0 you know the number is even
# otherwise the number is odd

if (getNum % 2) == 0:
    print ("{0} is Even number".format(getNum)) 
else:
    print("{0} is Odd number".format(getNum))

