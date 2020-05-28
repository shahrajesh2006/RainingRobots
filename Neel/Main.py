
import random
import time
from Player import Player

FORTNITE = open('Neel/Bestscore.txt', 'r') 
Lines = FORTNITE.readlines() 

# Strips the newline character 
for line in Lines: 
	print(line.strip()) 

NeelStealsSamsIdea = "y"
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



 WinningPlayer = players[0]# For now assume first player won
 print("For now the winning player is "+WinningPlayer.name)
 print(WinningPlayer)


 count = 0
 while count < int (GetOnePumped):
  time.sleep(1)
  print("looping for the player"+players[count].name)

  if players[count].tries < WinningPlayer.tries:
   WinningPlayer = players[count]#found a better player so switch
   print("Found the new winning player is "+WinningPlayer.name)
  else:
    print("Winning player is still the same "+WinningPlayer.name)
  count = count + 1

 print("The winner is...")
 time.sleep(2)
 print("The winner is " + WinningPlayer.name + "!!! Great Job!!!")
 
 WinningPlayer.printPlayerResults()

 FORTNITE = open('Neel/Bestscore.txt', 'w') 
 FORTNITE.writelines("Winner of the last game:"+ WinningPlayer.name+"\n")
 FORTNITE.writelines("Best Score for the last game:"+ str(WinningPlayer.tries)+"\n")
 FORTNITE.close() 
 
 time.sleep(3)
 NeelStealsSamsIdea= input("Would you like to play again(y for yes and n for no)")

 if NeelStealsSamsIdea == "n":
    break

