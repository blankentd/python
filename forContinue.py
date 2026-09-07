
# Continue statement

for num in range(2, 10): # Defined range of 2 to 10
    if num % 2 == 0: # If first number divided by 2 equals 0 the indicate an even number and continue
        print ("Found an even number", num)
        continue
    print ("Found an odd number", num) # Otherwise just indicate you found an odd number
