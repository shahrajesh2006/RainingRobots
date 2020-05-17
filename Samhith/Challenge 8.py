import random 
import os
import time
from Samhith.playerS import Player


# Using readlines() 
file1 = open('Rajesh/bestscore.txt', 'r') 
Lines = file1.readlines() 

# Strips the newline character 
for line in Lines: 
	print(line.strip()) 

#Line 1-2 are the random number and operating system module 
while True:
 numberofpeopleplaying = input("How many people are playing? The max is 10 players.")
 time.sleep(1)
 os.system("clear")



 players = []

 peopleplayingvalue = 0

 while peopleplayingvalue < int(numberofpeopleplaying):
  playersname = input("Player" + str(peopleplayingvalue + 1) + " what is your name or nickname")
  NewPerson = Player(playersname, random.randrange(1,101), 0)
  players.append(NewPerson)
  print ("New player created..."+players[peopleplayingvalue].name)
  peopleplayingvalue=peopleplayingvalue+1



 time.sleep(1)
 os.system("clear")
   

 peopleplayingvalue = 0
 while peopleplayingvalue < int(numberofpeopleplaying):
  players[peopleplayingvalue].PlayGame()
  peopleplayingvalue = peopleplayingvalue + 1

 time.sleep(1)
 os.system("clear")


 #This ask player 2 if they are ready
 print("Are")
 time.sleep(1)
 os.system("clear")
 print("you")
 time.sleep(1)
 os.system("clear")
 print("ready")
 time.sleep(1)
 os.system("clear")
 print("to see")
 time.sleep(1)
 os.system("clear")
 print("who")
 time.sleep(1)
 os.system("clear")
 print("won?")
 time.sleep(1)
 os.system("clear")
 input("Print any key to continue to continue")

 print("Then lets... see... who... wonnnnnnnnn!")
 time.sleep(1)
 os.system ("clear") #Clears screen


 WinningPlayer = players[0]# For now assume first player won
 peopleplayingvalue = 0
 while peopleplayingvalue < int (numberofpeopleplaying):
  time.sleep(1)
  if players[peopleplayingvalue].attempts < WinningPlayer.attempts:
   WinningPlayer = players[peopleplayingvalue]#found a better player so switch

 peopleplayingvalue = peopleplayingvalue + 1

 #With the above logic if there is tie then the first player will be the winner
  

 print("The winner is" + WinningPlayer.name)
 file1 = open('Rajesh/bestscore.txt', 'w') 
 file1.writelines("Winner of the last game:"+ WinningPlayer.name+"\n")
 file1.writelines("Best Score for the last game:"+ str(WinningPlayer.attempts)+"\n")
 file1.close() 
 Finish = input("Thank you for playing! Do you want to play again? If yes type y, if no press any other key")
 if Finish != "y":
  break
 

