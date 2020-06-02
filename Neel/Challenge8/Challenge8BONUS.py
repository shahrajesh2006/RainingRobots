import random
import time

from player import Player 

print("Welcome to the random number game")

# opens file 
File1 = open('Neel/Challenge8/bestscoreS.txt', 'r') 
File1Lines = File1.readlines() 

#reads file
for line in File1Lines: 
	print(line.strip()) 

file2 = open('Neel/Challenge8/Players.txt', 'r') 
sweat = file2.readlines() 
#reads the list of players

players =[] #create empty list of players when the program starts

# When you create player object you can add it to the list as shown below
#Lest assume 5 players want to play the games
count=0
GetOnePumped = int(input("How many players are playing "))
while count < GetOnePumped:
  playername= input("Player"+str(count+1)+ " what would you like your name to be:")
  NewPlayer = Player(playername, random.randrange(1,5), 0)
  NewPlayer.ExistPlayer(sweat)
  players.append(NewPlayer)
  count=count+1

print("Following player are signed up...Now lets play the Game")

count=0
while count < GetOnePumped:
  players[count].playGame()
  count=count+1 



players.sort(key=lambda x: x.tries, reverse=False)
 #With the above logic if there is tie then the first player will be the winner

print("The winner is" +players[0].name + "!!!!!")
time.sleep(1)
print("Here are the final results")
 
for x in range(int(GetOnePumped)):
  players[x].printPlayerResults()

file2 = open('Neel/Challenge8/Players.txt', 'w') 
for play in range (int(GetOnePumped)):
      file2.writelines(players[play].name+ "=" + str(players[play].tries) + "\n")
file2.close()
 
