## ----- open and write to file --------------

'''

file = open('test.txt', 'w')
test = file.write('Hello\n')
file.close()

'''

## ------ open file and read --------------

'''

file = open('test.txt', 'r')
test = file.read()
print(test)
file.close()

'''