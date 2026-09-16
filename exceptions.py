## --------- Exceptions --------------------

var1 = '1'
try:
   var1 = var1 + 1 # since var 1 is a string, it cannot be added to the number 1 
except:
   print(var1, " is not a number") # so we execute this
print(var1)