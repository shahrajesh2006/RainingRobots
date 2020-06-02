import random
import time
import os
from bonusplayer import Player

os.system("clear")

Bestscore = open('Aarav/bestscore1.txt', 'r') 
Lines = Bestscore.readlines()

C8BPlayers = open('Aarav/challenge8bonusplayers.txt', 'r')
BPlayersLines = C8BPlayers.readlines()

PlayNum = input("How many players are playing (no more than 10): ")

players = []

os.system("clear")

print("If you have played before, please enter the same name you used last time.")

PCiB = 0
while PCiB < int(PlayNum):
    PlayerName = input("Player " + str(PCiB + 1) + ", please enter your name: ")
    NP = Player(PlayerName, random.randint(1, 100), 0)
    players.append(NP)
    existingplayer = "n"
    for p in range(len(BPlayersLines)):
        y = BPlayersLines[p].split("=")
        if y[0] == PlayerName:
            print("Welcome back " + y[0] + ". Your previous score was " + y[1])
            existingplayer = "y"
            time.sleep(3)
    if existingplayer == "n":
        print("Welcome new player " + PlayerName)
        time.sleep(3)
    PCiB = PCiB + 1
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

Bestscore = open('Aarav/bestscore1.txt', 'w') 
Bestscore.writelines("The winner of the last game was: "+ players[0].name+"\n")
Bestscore.writelines("The best score of the last game was: "+ str(players[0].attempts)+"\n")
Bestscore.close()

C8BPlayers = open('Aarav/challenge8bonusplayers.txt', 'w')
C8BPlayers.writelines("")
C8BPlayers.close()

file2 = open('Aarav/challenge8bonusplayers.txt', 'w')
for n in range(int(PlayNum)):
    file2.writelines(players[n].name+"="+str(players[n].attempts)+"\n")
file2.close()