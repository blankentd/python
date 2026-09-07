
 # Open a file for input and reading
 
file = open('testfile.txt','w')
file.write('Hello World\n') 
file.write('How are you?') 
file.close()

file = open('testfile.txt', 'r') 
test = file.read()
print(test) 
file.close()
