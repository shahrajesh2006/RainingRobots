import random 
import os 
import time 
from player import Player

numberofplayers = input("Enter Number of Players | Max 10 : ")

time.sleep(1) 
os.system("clear") 

players = [] #Empty List

playersplayingvalue = 0

while playersplayingvalue < int(numberofplayers): 
  playersname = input("Player " + str(playersplayingvalue + 1) + " what is your username: ") 
  NewPlayer = Player(playersname, random.randrange(1,101), 0)
  players.append(NewPlayer)
  print ("Player Created | "+players[playersplayingvalue].name)
  playersplayingvalue = playersplayingvalue+1 

time.sleep(1) 
os.system("clear")

playersplayingvalue = 0

while playersplayingvalue < int(numberofplayers): 
  players[playersplayingvalue].playGame() 
  playersplayingvalue = playersplayingvalue + 1 
  
  print("The results are in... Lets see who won...") 
  
  time.sleep(10) 
  os.system ("clear") 
  
WinningPlayer = players[0]
playersplayingvalue = 0 
while playersplayingvalue < int (numberofplayers): 
  if players[playersplayingvalue].tries < WinningPlayer.tries:
    WinningPlayer = players[playersplayingvalue] 
  playersplayingvalue = playersplayingvalue + 1

  print("Winner | " + WinningPlayer.name)

  time.sleep(2) 
  os.system("clear") 
      
  print("Thank You For Playing")

  time.sleep(1)
