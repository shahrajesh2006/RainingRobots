import random
import time
import os
from player import Player

# Lets print the best score from last game
Bestscore = open('Aarav/bestscore.txt', 'r') 
Lines = Bestscore.readlines() 
for line in Lines: 
	print(line.strip())

PlayNum = input("How many players are playing (no more than 10): ")

players = []

os.system("clear")

PCiB = 0
while PCiB < int(PlayNum):
  PlayerName = input("Player " + str(PCiB + 1) + ", please enter your name: ")
  NP = Player(PlayerName, random.randint(1, 100), 0)
  PCiB = PCiB + 1
  players.append(NP)
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

players.sort(key=lambda x: x.attempts, reverse=False)

print("The winner is about to be announced...")
time.sleep(2)
print("The winner is " + players[0].name + "!!! Great Job!!!")
time.sleep(2)
print("The results are about to be announced...")

for n in range(int(PlayNum)):
  players[n].playerResults()

# Lets save the best score from this game

Bestscore = open('Aarav/bestscore.txt', 'w') 
Bestscore.writelines("The winner of the last game was: "+ players[0].name+"\n")
Bestscore.writelines("The best score of the last game was: "+ str(players[0].attempts)+"\n")
Bestscore.close()