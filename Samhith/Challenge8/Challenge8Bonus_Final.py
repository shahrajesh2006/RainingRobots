import random 
import os
import time
from player import Player
#Line 1 imports random module, line 2 imports operating system module, line 3 imports time module, and line 4 imports local player module


# opens file 
file1 = open('Samhith/Challenge8/bestscoreS.txt', 'r') 
Lines = file1.readlines() 

# Strips and reads file
for line in Lines: 
	print(line.strip()) 

file2 = open('Samhith/Challenge8/Players.txt', 'r') 
players2 = file2.readlines() 
#reads the list of players
 
while True:
 numberofpeopleplaying = input("How many people are playing? The max is 10 players.")#asks how many people are playing
 time.sleep(1)
 os.system("clear")
 #Waits 1 second and clears screen



 players = []# creates empty list

 peopleplayingvalue = 0

 while peopleplayingvalue < int(numberofpeopleplaying):
  playersname = input("Player" + str(peopleplayingvalue + 1) + " what is your name or nickname")
  NewPerson = Player(playersname, random.randrange(1,101), 0)
  NewPerson.checkExisitingPlayer(players2) # check if it is an existing player
  players.append(NewPerson)
   
  print (players[peopleplayingvalue].name + "is now in the game!!!")
  peopleplayingvalue=peopleplayingvalue+1
  #line 28-33 asks what there name is and repeats based on how many people are playing and prints whoever just entered their name is now in the game



 time.sleep(1)
 os.system("clear")
 #Waits 1 second and clears screen
   

 peopleplayingvalue = 0
 while peopleplayingvalue < int(numberofpeopleplaying):
  players[peopleplayingvalue].PlayGame()
  peopleplayingvalue = peopleplayingvalue + 1
#this creates the game for whoever is playing

 time.sleep(1)
 os.system("clear")
 #Waits 1 second and clears screen


 #below asks whether they are ready to see who won
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
 input("Press any key to continue to continue")

 print("Then lets... see... who... wonnnnnnnnn!")
 #time.sleep(1)
 #os.system ("clear") 
 #Waits 1 second and clears screen


 WinningPlayer = players[0]
 peopleplayingvalue = 0
 while peopleplayingvalue < int (numberofpeopleplaying):
  time.sleep(1)
  if players[peopleplayingvalue].attempts < WinningPlayer.attempts:
   WinningPlayer = players[peopleplayingvalue]
  peopleplayingvalue = peopleplayingvalue + 1
 #line 81-88 makes the first player the winner and compares them with the other players and if they found a person with lower attempts and then they become the comparer

 
 

 print("The winner is" + WinningPlayer.name + "!!!!!")
 time.sleep(2)
 os.system("clear")
 file1 = open('Samhith/Challenge8/bestscoreS.txt', 'w') 
 file1.writelines("Winner of the last game:"+ WinningPlayer.name+"\n")
 file1.writelines("Best Score for the last game:"+ str(WinningPlayer.attempts)+"\n")
 file1.close()
 file2 = open('Samhith/Challenge8/Players.txt', 'w') 
 for play in range (int(numberofpeopleplaying)):
      file2.writelines(players[play].name+ "=" + str(players[play].attempts) + "\n")
 
 file2.close()  
 #94-98 prints who won and the lowest number of attempts
 time.sleep(5)
 os.system("clear")
 for results in range(int(numberofpeopleplaying)):
  players[results].PlayerResults()
 #line 104-105 prints the final results of the game
 time.sleep(10)
 os.system("clear")
 Finish = input("Thank you for playing! Do you want to play again? If yes type y, if no press any other key")
 time.sleep(2)
 os.system("clear")
 if Finish != "y":
  break
 

