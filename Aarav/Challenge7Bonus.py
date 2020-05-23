import random
import time
import os
from bonusplayer import Player

PlayNum = input("How many players are playing (no more than 10): ")

players = []

os.system("clear")

PCiB = 0
while PCiB < int(PlayNum):
  PlayerName = input("Player " + str(PCiB + 1) + ", please enter your name: ")
  NP = Player(PlayerName, random.randint(1, 100), 0)
  PCiB = PCiB + 1
  players.append(NP)
  #os.system("clear")

time.sleep(3)
os.system("clear")

PCiB = 0
while PCiB < int(PlayNum):
  time.sleep(1)
  os.system("clear")
  players[PCiB].playGame()
  PCiB = PCiB + 1

print("Give me a second to calculate the winner.")

time.sleep(2)
os.system("clear")

players.sort(key=lambda x: x.attempts, reverse=False)#Sorting By attempts lower to highest

print("The winner is about to be announced...")
time.sleep(2)

if players[0].isitaTie(players):
    print("It is a tie. There is no winner")
    for n in range(int(PlayNum)):
        players[n].playerResults()
else:
    print("The winner is " + players[0].name + "!!! Great Job!!!")