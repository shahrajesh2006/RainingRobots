import random 
import os 
import time 
from Player import Player

Bestscore = open('Vir/Challenge8Bonus/bestscores.txt', 'r') 
Lines = Bestscore.readlines() 

for line in Lines: 
	print(line.strip())

#reads the list of players
OGPlayers = open('Vir/Challenge8Bonus/players.txt', 'r') 
Lines2 = OGPlayers.readlines() 


time.sleep(3)
os.system("clear")

numberofplayers = input("Enter Number of Players | Max 10 : ")

time.sleep(1) 
os.system("clear") 

players = [] #Empty List

playersplayingvalue = 0

while playersplayingvalue < int(numberofplayers): 
  playersname = input("Player " + str(playersplayingvalue + 1) + " what is your username: ") 
  NewPlayer = Player(playersname, random.randrange(1,101), 0)
  players.append(NewPlayer)#Adding new player to the list
  NewPlayer.checkExisitingPlayer(Lines2) # check if it is an existing player
  players.append(NewPlayer)

  print ("Player Created | "+ players[playersplayingvalue].name)
  playersplayingvalue = playersplayingvalue+1 

time.sleep(1) 
os.system("clear")

playersplayingvalue = 0

while playersplayingvalue < int(numberofplayers): 
  players[playersplayingvalue].playGame() 
  playersplayingvalue = playersplayingvalue + 1

print("The results are in... Lets see who won...")

time.sleep(2)
os.system("clear")

players.sort(key=lambda x: x.tries, reverse=False)
 #With the above logic if there is tie then the first player will be the winner

print("Winner | " +players[0].name)

time.sleep(1)
os.system("clear")

print("Here are the final results")
 
for x in range(int(numberofplayers)):
  players[x].printPlayerResults()

time.sleep(10)
os.system("clear")

print("Thank You For Playing")

time.sleep(1)

Bestscore = open('Vir/Challenge8Bonus/bestscores.txt', 'w') 
Bestscore.writelines("Winner of the last game: " + players[0].name+"\n")
Bestscore.writelines("Best Score for the last game: " + str(players[0].tries)+"\n")
Bestscore.close()

OGPlayers = open('Vir/Challenge8Bonus/players.txt', 'w') 
for play in range(int(numberofplayers)):
    OGPlayers.writelines(players[play].name+ "=" + str(players[play].tries) + "\n")
OGPlayers.close()