#importing objects for later
import random
from Challenge7Player import Player
import os
import time

players = []

#UI = "y"
#while UI == "y":
numberOfPeoplePlaying = int (input("The max is 10 players. That being said, how many people are playing?"))

time.sleep(2)
os.system("clear")

peoplePlayingValue = 0

while peoplePlayingValue < int(numberOfPeoplePlaying):
  playersName = input("Alright Player, " + str(peoplePlayingValue + 1) + " how would you like to be known?")
  newPlayer = Player(playersName, random.randrange(1,101), 0)
  players.append(newPlayer)
  print("Welcome " + players[peoplePlayingValue].playerName + "!")
  peoplePlayingValue = peoplePlayingValue + 1

time.sleep(2)
os.system("clear")

peoplePlayingValue = 0
while peoplePlayingValue < int(numberOfPeoplePlaying):
  players[peoplePlayingValue].playGame()
  peoplePlayingValue = peoplePlayingValue + 1

start = input("Are you ready to see who won yet?")
if start.lower().strip() == "y":
  print("Well, what are we waiting for then? Let's see who won!")
  time.sleep(2)
  os.system("clear")

  winningPlayer = players[0]#lets assume that player 1 won
  peoplePlayingValue = 0
  while peoplePlayingValue < int (numberOfPeoplePlaying):
    if players[peoplePlayingValue].numberOfAttempts < winningPlayer.numberOfAttempts:
      winningPlayer = players[PeoplePlayingValue]#checks if there is a better player
    peoplePlayingValue = peoplePlayingValue + 1

    print("And the winner...")
    time.sleep(2)
    print(winningPlayer.playerName + "!")
    print("You're number was " +  str (winningPlayer.randomNumber) + " and it took you " + str (winningPlayer.numberOfAttempts) + " attempts to find it!")
    print("Thank you all for playing!")
    break
