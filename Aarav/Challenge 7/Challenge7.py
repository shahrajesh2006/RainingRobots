import random
import time
import os
from player import Player

PlayNum = input("How many players are playing (no more than 10): ")

players = []

os.system("clear")

PCiB = 0
while PCiB < int(PlayNum):
  PlayerName = input("Player " + str(PCiB + 1) + ", please enter your name: ")
  NP = Player(PlayerName, random.randint(1, 100), 0)
  PCiB = PCiB + 1
  players.append(NP)
  time.sleep(1)
  os.system("clear")

time.sleep(1)
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

WinnerP = players[0]
PCiB = 0
while PCiB < int (PlayNum):
  if players[PCiB].attempts < WinnerP.attempts:
    WinnerP = players[PCiB]
  PCiB = PCiB + 1


print("The winner is about to be announced...")
time.sleep(2)
print("The winner is " + WinnerP.name + "!!! Great Job!!!")
