import random
import time
import os
from Challenge8Player import Player

os.system("clear")

# Lets print the best score from last game
bestScore = open('Vihaan/Challenge 8/bestScore.txt', 'r') 
Lines = bestScore.readlines() 
for line in Lines: 
	print(line.strip())
time.sleep(2)

numberOfPeoplePlaying = int (input("The max is 10 players. That being said, how many people are playing?"))

players = []

time.sleep(2)
os.system("clear")

peoplePlayingValue = 0
while peoplePlayingValue < int(numberOfPeoplePlaying):
  PlayerName = input("Player " + str(peoplePlayingValue + 1) + ", please enter your name: ")
  NP = Player(PlayerName, random.randint(1, 100), 0)
  peoplePlayingValue = peoplePlayingValue + 1
  players.append(NP)

time.sleep(1)
os.system("clear")

peoplePlayingValue = 0
while peoplePlayingValue < int(numberOfPeoplePlaying):
  time.sleep(1)
  os.system("clear")
  players[peoplePlayingValue].playGame()
  peoplePlayingValue = peoplePlayingValue + 1

print("Just one moment...")

time.sleep(2)
os.system("clear")

players.sort(key=lambda x: x.numberOfAttempts, reverse=False)

start = input("Are you ready to see who won yet?")
if start.lower().strip() == "y":
  print("Well, what are we waiting for then? Let's see who won!")
  time.sleep(3)
  os.system("clear")

  winningPlayer = players[0]#lets assume that player 1 won
  peoplePlayingValue = 0
  while peoplePlayingValue < int (numberOfPeoplePlaying):
    if players[peoplePlayingValue].numberOfAttempts < winningPlayer.numberOfAttempts:
      winningPlayer = players[PeoplePlayingValue]#checks if there is a better player
    peoplePlayingValue = peoplePlayingValue + 1

print("And the winner is...")
time.sleep(3)
print(winningPlayer.playerName + "!")
time.sleep(2)
print(winningPlayer.playerScore())

# Lets save the best score from this game

bestScore = open('Vihaan/Challenge 8/bestscore1.txt', 'w') 
bestScore.writelines("Last game's winner was "+ players[0].playerName + "\n")
bestScore.writelines("Last game's best score was "+ str(players[0].numberOfAttempts) + "\n")
bestScore.close()