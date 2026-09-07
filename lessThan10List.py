#!/usr/bin/python

import os, sys

## ----- Program will print out all the elements of a list that are 
## less than 10 ------

showList = [1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89] # Defined list
for i in showList: # Loop through list starting at the first element
    if i < 10: # If the element is less than 10, display it otherwise do not display it
       print i

