import random
import os
import time
from player import Player


print("Welcome to the random number game")

#Here is the way I get the name
Player1name= input("Player 1, what would you like your name to be:")

P1 = Player(Player1name, random.randrange(1,101), 0)

Player2name= input("Player 2, what would you like your name to be:")

P2 = Player(Player2name,  random.randrange(1,101), 0)

P1.playGame()

time.sleep(2)

os.system ("clear")

P2.playGame()

time.sleep(2)

os.system ("clear")

#Here I am writing the winner
if P1.tries < P2.tries:
  print("The winner is " + Player1name)
elif P1.tries > P2.tries:
  print("The winner is " + Player2name)
elif P1.tries == P1.tries:
  print("Its a tie")
print("----------------------------------")

#Here I am writing the final stats
print("Here are the final results")
P1.printPlayerResults()
P2.printPlayerResults()
