# Rock crushes scissors
# Rock crushes lizard
# Paper covers rock
# Paper disproves Spock
# Scissors cuts paper
# Scissors decapitate lizard
# Lizard poisons Spock
# Lizard eats paper
# Spock vaporizes rock
# Spock smashes scissors 

# Include a 'quit' function

rock = 'rock'
paper = 'paper'
scissors = 'scissors'
lizard = 'lizard'
spock = 'Spock'

print("")
print ("Welcome to the Rock, Paper, Scissors, Lizard, Spock game")
print("")

answer1 = 0
answer2 = 0

while answer1 > 5 or answer1 < 1:
   try:
      answer1 = int(input("Player 1 please type 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for Spock: "))
      print("")
            
   except ValueError:
      print ("You must provide an integer value between 1 and 5")
      print("")

while answer2 > 5 or answer2 < 1:
   try:
      answer2 = int(input("Player 2 please type 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for Spock: "))
      print("")

   except ValueError:
      print ("You must provide and integer value between 1 and 5")
      print("")

   if answer1 == 1 and answer2 == 1:
      print ("Player 1 and 2 tie! ")
   elif answer1 == 1 and answer2 == 2:
      print ("Player 2 wins because paper covers rock! ")
   elif answer1 == 1 and answer2 == 3:
      print ("Player 1 wins because rock crushes scissors! ") 
   elif answer1 == 1 and answer2 == 4:
      print ("Player 1 wins because rock crushes lizard! ")
   elif answer1 == 1 and answer2 == 5:
      print ("Player 2 wins because Spock vaporizes rock! ")
   elif answer1 == 2 and answer2 == 1:
      print ("Player 2 wins because paper covers rock! ")
   elif answer1 == 2 and answer2 == 2:
      print ("Player 1 and 2 tie! ")
   elif answer1 == 2 and answer2 == 3:
      print ("Player 2 wins because scissors cuts paper! ")
   elif answer1 == 2 and answer2 == 4:
      print ("Player 2 wins because lizard eats paper! ")
   elif answer1 == 2 and answer2 == 5:
      print ("Player 1 wins because paper disproves Spock! ")
   elif answer1 == 3 and answer2 == 1:
      print ("Player 1 wins because rock crushes scissors! ")
   elif answer1 == 3 and answer2 == 2:
      print ("Player 1 wins because scissors cuts paper! ")
   elif answer1 == 3 and answer2 == 3:
      print ("Player 1 and 2 tie! ")
   elif answer1 == 3 and answer2 == 4:
      print ("Player 1 wins because scissors decapitate lizard! ")
   elif answer1 == 3 and answer2 == 5:
      print ("Player 2 wins because Spock smashes scissors! ")
   elif answer1 == 4 and answer2 == 1:
      print ("Player 2 wins because rock crushes lizard! ")
   elif answer1 == 4 and answer2 == 2:
      print ("Player 1 wins because lizard eats paper! ")
   elif answer1 == 4 and answer2 == 3:
      print ("Player 3 wins because scissors decapitate lizard! ")
   elif answer1 == 4 and answer2 == 2:
      print ("Player 1 and 2 tie! ")
   elif answer1 == 4 and answer2 == 5:
      print ("Player 1 wins because lizard poisons Spock! ")
   elif answer1 == 5 and answer2 == 1:
      print ("Player 1 wins because Spock vaporizes rock! ")
   elif answer1 == 5 and answer2 == 2:
      print ("Player 2 wins because paper disproves Spock! ")
   elif answer1 == 5 and answer2 == 3:
      print ("Player 1 wins because Spock crushes scissors! ")
   elif answer1 == 5 and answer2 == 4:
      print ("Player 2 wins because lizard poisons Spock! ")
   elif answer1 == 5 and answer2 == 5:
      print ("Player 1 and 2 tie! ")
