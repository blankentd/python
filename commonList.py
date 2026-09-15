#!/usr/bin/python

import os, sys

## ----- Program will take two lists and print out all the elements that are common between the two lists ------

listOne = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listTwo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_member(listOne, listTwo): # devines a function with both lists as arguments
    a_set = set(listOne) # Create a set consisting of the elements in the listOne list
    b_set = set(listTwo) # Create a set consisting of the elements in the listTwo list
    if (a_set & b_set): # If both sets exist 
        print(list(a_set & b_set)) # convert set to a list to eliminate set in output
    else:
        print("no common elements") 

common_member(listOne, listTwo) # Call the common_member function
