import random 
import os
import time
from player import Player
#Line 1-2 are the random number and operating system module 

numberofplayers = input("How many players want to play- max 10")

#Here is the object with three arguments
players = []

peopleplayingvalue = 0
while peopleplayingvalue < int(numberofplayers):
  print("Player" + str(peopleplayingvalue + 1) + " what is your name or a nickname.")
  playersname=input("Enter here:") 
  NewPerson = Player(playersname, random.randrange(1,101),0)
  players.append(NewPerson)
  peopleplayingvalue = peopleplayingvalue + 1
   

peopleplayingvalue = 0
while peopleplayingvalue < int(numberofplayers):
  players[peopleplayingvalue].PlayGame()
  peopleplayingvalue = peopleplayingvalue + 1
  time.sleep(2)
  os.system ("clear")




# Now lets identify who won. For this we need find player object which has least number of attempts
peopleplayingvalue = 0
winnerNumberofAttempts=players[0].attempts#lets assume winner number of attempts is first player
winnerPlayer=0 # lets assume first player is the winner for now
while peopleplayingvalue < int(numberofplayers):
    if players[peopleplayingvalue].attempts<winnerNumberofAttempts:
      winnerNumberofAttempts=players[peopleplayingvalue].attempts
      winnerPlayer=peopleplayingvalue


#This ask player 2 if they are ready
Ready = input("Are you ready to find who won? Type y to continue")
if Ready.lower().strip() =="y": 
 print ("Ok, lets continue!")

time.sleep(1)
os.system ("clear") #Clears screen

print("Winner is:"+players[winnerPlayer].name)



#Here I am writing the final stats
print("Here are the final results")

peopleplayingvalue = 0
while peopleplayingvalue < int(numberofplayers):
  players[peopleplayingvalue].PlayerResults()
  
