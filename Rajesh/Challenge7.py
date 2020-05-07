import random 
import os
import time
from player import Player
#Line 1-2 are the random number and operating system module 
numberofpeopleplaying = input("How many people are playing? The max is 10 players.")
time.sleep(1)
os.system("clear")


#Here is the object with three arguments
players = []

peopleplayingvalue = 0

while peopleplayingvalue < int(numberofpeopleplaying):
 playersname = input("Player" + str(peopleplayingvalue + 1) + " what is your name or nickname")
 NewPerson = Player(playersname, random.randrange(1,101), 0)
 players.append(NewPerson)
 print ("New player created..."+players[peopleplayingvalue].name)
 peopleplayingvalue=peopleplayingvalue+1


# players.append(NewPerson)
# peopleplayingvalue = peopleplayingvalue + 1
time.sleep(1)
os.system("clear")
   

peopleplayingvalue = 0
while peopleplayingvalue < int(numberofpeopleplaying):
  players[peopleplayingvalue].PlayGame()
  print ("after game")
  peopleplayingvalue = peopleplayingvalue + 1


#This ask player 2 if they are ready
print("Are")
time.sleep(1)
print("you")
time.sleep(1)
print("ready")
time.sleep(1)
print("to see")
time.sleep(1)
print("who")
time.sleep(1)
print("won?")
ready = input("Print y to continue")

if ready.lower().strip() =="y": 
  print("Then lets... see... who... wonnnnnnnnn!")
time.sleep(1)
os.system ("clear") #Clears screen


WinningPlayer = players[0]# For now assume first player won
print("For now the winning player is "+WinningPlayer.name)
print(WinningPlayer)


peopleplayingvalue = 0
while peopleplayingvalue < int (numberofpeopleplaying):
  time.sleep(1)
  print("looping for the player"+players[peopleplayingvalue].name)
  if players[peopleplayingvalue].attempts < WinningPlayer.attempts:
   WinningPlayer = players[peopleplayingvalue]#found a better player so switch
   print("Found the new winning player is "+WinningPlayer.name)
  else:
    print("Winning player is still the same "+WinningPlayer.name)
  peopleplayingvalue = peopleplayingvalue + 1

#With the above logic if there is tie then the first player will be the winner
  

print("The winner is" + WinningPlayer.name)
