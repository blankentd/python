#!/usr/bin/python

import os, sys

## ----- Program will ask a user for a number and indicate whether it is prime or not ----- 

myNum = int(input("Give me a number: "))

if myNum > 1:
    for i in range(2, myNum//2): # Start with 2 and divide by the result of myNum divided by 2
        if (myNum % i) == 0:
            print(myNum, "is not a prime number")
            break
    else:
        print(myNum, "is a prime number.")
else:
    print(myNum, "is not a prime number.")
