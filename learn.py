## -------- Sets -----------------------
## Once you create a set you cannot change it but you can add to it with union or update

'''
a = (("apple", "banana", "cherry"))
print(a)

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