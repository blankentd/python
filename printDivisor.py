#!/usr/bin/python

import os, sys

## ----- Program will accept a number and print out a list of divisors of the number 

i = 1

getNumber = int(input("Provide a number: "))

while i < getNumber:
   if getNumber % i == 0:
      print(' divisor ', i)
   i = i + 1
