import random
import os

print("Welcome to the random number game")

#This is the variables that coumt th number of attempts
P1c=1
P2c=1

#Here is the way I get the name
Player1name= input("Player 1, what would you like your name to be:")
Player2name= input("Player 2, what would you like your name to be:")


os.system ("clear")

#Here is the randomnumber number generated for each player
randomnumberP1 = random.randrange(1,101)
randomnumberP2 = random.randrange(1,101)

#Here is th game part of the function.
NI = "y"
while NI == "y":
 x = int (input("Guess a number between 1 and 100:"))
 if x > randomnumberP1:
  print("That was to high.")
  P1c = P1c + 1
 elif x < randomnumberP1:
  print("That was too low")
  P1c = P1c + 1
 else:
  print ("Well done, you got it")
  break

#This ask player 2 if they are ready
YesnoP1 = input("Player 2 ready?")
if YesnoP1 =="y" or "Y":
 print ("Ok lets go")
os.system ("clear")

#Here is the game for player 2 
NI = "y"
while NI == "y":
 x = int (input("Guess a number between 1 and 100:"))
 if x > randomnumberP2:
  print("That was to high.")
  P2c = P2c + 1
 elif x < randomnumberP2:
  print("That was too low")
  P2c = P2c + 1
 else:
  print ("Well done, you got it")
  break

#Here is the objects of the players
#P1 = Player(Player1name, str(randomnumberP1), str(P1c))
#P2 = Player(Player2name, str(randomnumberP2), str(P2c))
os.system ("clear")

#Here I am asking to say if they are ready for the winner
YesnoP2 = input("Are we ready to see who won(type y to continue)?")
if YesnoP2 =="y" or "Y":
 print ("Drumroll please")
os.system ("clear")

#Here I am writing the winner
if P1c < P2c:
  print("The winner is " + Player1name)
elif P1c > P2c:
  print("The winner is " + Player2name)
elif P1c == P2c:
  print("Its a tie")
print("----------------------------------")

#Here I am writing the final stats
print("Here are the final results")
print("Player1:")
print("Hi"+Player1name)
print("Your random number was"+randomnumberP1)
print("Your number of attempts was was"+P1c)

print("Player2:")
print("Hi"+Player2name)
print("Your random number was"+randomnumberP2)
print("Your number of attempts was was"+P2c)
