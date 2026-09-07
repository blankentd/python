#!/usr/bin/python

import os, sys

## ----- Program take a list, creats a new one and with only even elements in it -----

listOne = [1, 4, 9, 16, 25, 36, 49, 81, 100] # Define the list contents

# Generate a second list by reading each element and dividing it by two. If the result is zero print the value
# because it is even

listTwo = [element for element in listOne if element % 2 == 0]; print(listTwo) 

