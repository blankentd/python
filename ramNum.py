#!/usr/bin/python

import os, sys, random

## ----- Program will generate a random number and ask a user to guess. User can type exit to quit ------

count = 0
guess = 0
randomNum = random.randint(2, 6)

while guess != randomNum and guess != "exit":
    guess = input("Please type a number: ")

    if guess == "exit":
        break    

    guess = int(guess)
    count += 1

    if guess < randomNum:
        print("Too low!")
    elif guess > randomNum:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")

 
