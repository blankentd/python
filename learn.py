#!/usr/bin/python

## This script is for practicing Python coding
## Use python -V to get version. My version is 3

# One line comment

# Three ' are used for multi line comments

import os, sys

## ------- Testing Strings ----------------

'''

a = "string"
b = "STRING"
print "This prints tr: " + (a[1:3])  # prints 'tr' 
print "This prints strin: " + (a[:-1])  # prints 'strin' (calculates from end to beginning because of -)
print (a.count('r'))  # counts number of r's
print (a.find('r'))  # prints location of r in the string (starting a 0)
print "This prints the string in lowercase: " + (b.lower())  # prints string in lowercase
print "This prints the string in uppercase: " + (a.upper())  # prints string in upper case
print "This replaces one character with another :" + (a.replace('r','z'))  # replaces one character with another and prints result
print "This removes a specified character from the string: " + (a.strip('g'))  # removes specified character from string and prints result

'''

## -------- Testing Lists (Arrays in Python) -----------
## A list is a collectionwhich is ordered and changeable

'''
sampleList = [1,2,3,4,5,6,7,8]
print (sampleList[1])  #Prints the value in the list that is in the 1 location (starts at 0)
print ""
sampleList = [1,2,3,4,5,6,7,8]  #Prints each value in the list staring at 0
for a in sampleList:
   print (a)

'''

## ------ Prints list content and adds the append value -------

'''

sampleList = [1,2,3,4,5,6,7,8]
sampleList.append(9)  #Appends a 9 to the list
print(sampleList)

'''

## ------- Prints a specific value from the list -------------

'''
sampleList = [1,2,3,4,5,6,7,8]  #Prints a specific value from the list
print (sampleList[7])

'''

## ------ Prints number where defined value is in the array ------

'''
sampleList = [1,2,3,4,5,6,7,8]
print(sampleList.count(2))

'''

## ------ Prints value at index location ---------------

'''
sampleList = [1,2,3,4,5,6,7,8]
print(sampleList.index(3))

'''

## ----- replaces a value into the list at the specifed value ------

'''
sampleList = [1,2,3,4,5,6,7,8]
sampleList.insert(3,11)
print(sampleList)

'''

## ----- removed value at specific location ----------------

'''
sampleList = [1,2,3,4,5,6,7,8]
sampleList.remove(1)
print(sampleList)

'''

## ----- Reverse list ------------

'''
sampleList = [1,2,3,4,5,6,7,8]
sampleList.reverse()
print(sampleList)

'''

## ----- Sorting list -------------

'''
sampleList = [1,2,3,4,5,6,7,8]
sampleList.sort()
print(sampleList)

'''

## ---- Prints list in reverse order --------

'''

sampleList = [1,2,3,4,5,6,7,8]
sampleList.sort(reverse = True)
print(sampleList)

'''

## ----- Prints value at specified location --------

'''

sampleList = [1,2,3,4,5,6,7,8]
x = sampleList.pop(3)
print(x)

'''

## ----- Appends specified value to list -----------

'''

sampleList = [1,2,3,4,5,6,7,8]
sampleList.append(9)
print(sampleList)

'''

## -------- Prints the tuple ---------
## A tuple is a collection which is ordered and unchangeable

'''

myTuple = (1,2,3)
print (myTuple) # Prints the tuple

'''

## ----- This should not work because you can't modify a tuple --------

'''

myTuple = (1,2,3)
myTuple.append(4)
print (myTuple)

'''

## ---- This creates a tuple, modifies it as a list and appends to the list and then prints ----

'''

myTuple = (1,2,3)
myList = list(myTuple)
myList.append(4)
print (myList)

'''

## A set is a collection which is unordered and unindexed

## -------- if-then --------------------------

'''

answer = None
x = 1
answer = int(input("Please type a number: "))
if answer > 9:
   x = answer * answer
   print(x)
else:
   x = x + answer 
   print (x) 

'''

## -------- while-loop --------------------

'''

answer = None
answer = int(input("Please type a number: "))
while answer < 10 and answer != 0:
   print (answer)
   answer = answer + 1

'''

## -------- for-loop ----------------------

'''
sum = 1
answer = 100

for counter in range(sum,6):
   print (counter) 

'''

## ----- open a file for input --------------

'''

file = open('test.txt', 'w')
test = file.write('Hello\n')
file.close()

'''

## ------ open file for input --------------

'''

file = open('test.txt', 'r')
test = file.read()
print(test)
file.close()

'''

## ---- This code prints each letter of the word 'python' on separate line --- 

'''

answer = None

for answer in 'Python.':
   if answer == '.':
      break
   print(answer)

'''

## ---- This code prints a statement about even and odd numbers ----

'''
answer = None

for answer in range(2, 10):
   if answer % 2 == 0:
      print ("Found an even number", answer)
      continue
   print ("Found an odd number", answer)	  

'''

## ---- This code prints a Fibonacci series up to n. ----- 

'''

def fib(n):
   a, b = 0, 1
   while a < n:
      print (a,)
      a, b = b, a+b
		
fib(2000)

'''

## -------- Dictionaries --------------------
## A Dictionary is a collection that is unordered, changeable and indexed

'''

myExample = {'someItem': 2, 'otherItem': 20}
print(myExample['otherItem'])

myExample = {'someItem': 2, 'otherItem': 20}
myExample['newItem'] = 400
for a in myExample:
   print(a)

myExample = {'someItem': 2, 'otherItem': 20, 'newItem': 400}
for a in myExample:
   print (a, myExample[a])

'''
## -------- Sets -----------------------
## Once you create a set you cannot change it but you can add to it with union or update

'''
a = (("apple", "banana", "cherry"))
print(a)

'''

## -------- String formatting --------------

'''

print('The order total comes to %f' % 123.44) #f is short for float
print('The order total comes to %.2f' % 123.444)

a = "abcdefghijklmnopqrstuvwxyz"

print('%.20s' % a)

'''

## --------- Exceptions --------------------

'''

var1 = '1'
try:
   var1 = var1 + 1 # since var 1 is a string, it cannot be added to the number 1 
except:
   print(var1, " is not a number") # so we execute this
print(var1)

'''

# ----- The string is casted as an integer before adding and it completes the addition without error ---

'''

var1 = '1'
try:
   var2 = var1 + 1 # since var1 is a string, it cannot be added to the number 1
except:
   var2 = int(var1) + 1
print(var2)

'''

# -------------- ClassOne.py -------------------

'''
class Calculator(object):
   #define class to simulate a simple calcularor
   def __init__ (self):
      #start with zero
      self.current = 0
   def add(self, amount):
      #add number to current
      self.current += amount
   def getCurrent(self):
      return self.current

from ClassOne import * #get classes from ClassOne file
myBuddy = Calculator() # make myBuddy into a Calculator object
myBuddy.add(2) # use myBuddys new add method derived from the Calculator class
print(myBuddy.getCurrent()) #print myBuddy's current instance variable

'''
