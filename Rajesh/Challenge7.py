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



players.sort(key=lambda x: x.attempts, reverse=False)


peopleplayingvalue = 0
while peopleplayingvalue < int (numberofpeopleplaying):
  print(players[peopleplayingvalue].name+":"+str(players[peopleplayingvalue].attempts))
  peopleplayingvalue = peopleplayingvalue + 1

#With the above logic if there is tie then the first player will be the winner
