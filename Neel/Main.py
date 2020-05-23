
import random
import time
from player import Player 
FORTNITE = open('Neel/Bestscore.py', 'r') 
Lines = FORTNITE.readlines() 

# Strips the newline character 
for line in Lines: 
	print(line.strip()) 

NeelStealsSamsIdea == "y"
while NeelStealsSamsIdea== "y":
 print("Welcome to the random number game")

 players =[] #create empty list of players when the program starts

# When you create player object you can add it to the list as shown below
#Lest assume 5 players want to play the games
 count=0
 GetOnePumped = int(input("How many players are playing"))
 while count < GetOnePumped:
  playername= input("Player"+str(count+1)+ " what would you like your name to be:")
  NewPlayer = Player(playername, random.randrange(1,40), 0)
  players.append(NewPlayer)
  count=count+1

 print("Following player are signed up...Now lets play the Game")

 count=0
 while count < GetOnePumped:
  players[count].playGame()
  count=count+1 



 count = players[0]
 Neel = 0
 while Neel < int (GetOnePumped):
  if players[count].attempts < Neel.attempts:
    Neel = players[count]
  count = count + 1


 print("The winner is...")
 time.sleep(2)
 print("The winner is " + Neel.name + "!!! Great Job!!!")
 time.sleep(3)
NeelStealsSamsIdea= input("Would you like to play again(y for yes and n for no)")
if NeelStealsSamsIdea == "n":
      break
print("The winner is" + Neel.name)
FORTNITE = open('Rajesh/bestscore.txt', 'w') 
FORTNITE.writelines("Winner of the last game:"+ Neel.name+"\n")
FORTNITE.writelines("Best Score for the last game:"+ str(Neel.attempts)+"\n")
FORTNITE.close() 