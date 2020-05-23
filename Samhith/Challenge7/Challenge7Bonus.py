import random
import os
import time
from player import Player
#Line 1-2 are the random number and operating system module
Ui = "c" 
while Ui == "c":
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
 #With the above logic if there is tie then the first player will be the winner

 print("The winner is" +players[0].name + "!!!!!")
 time.sleep(1)
 os.system("clear")
 print("Here are the final results")
 
 for x in range(int(numberofpeopleplaying)):
  players[x].PlayerResults()

 print("Thank you for playing the random number game!!!!")
 time.sleep(1)
 Ui = input("Do you want to play again. Type c if you do. If not, type anything except c")
 if Ui.lower().strip() != "c":
  break
 time.sleep(1)
 os.system("clear")
 print("Thank you for playing the random number game!!!!")
 time.sleep(1)
 Ui = input("Do you want to play again. Type c if you do. If not, type anything except c")
 if Ui.lower().strip() != "c":
  break
  #Line 77 through 79 asks whether they want to play again and if yes, then it restarts the game, or if they don't want to play it will end the game.
