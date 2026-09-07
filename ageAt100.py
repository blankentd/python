#!/usr/bin/python

import os, sys, datetime

## ----- Program asks user for their name and age and prints out a message
## ----- to them and tells them the year they will turn 100 years old ------

now = datetime.datetime.now()

getName = raw_input("Please enter your name: ")
getAge = int(input("Please enter your age: "))
print "Hi, " + getName + ". " + "You will turn 100 on the year", (now.year-getAge+100) 



