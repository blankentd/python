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