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