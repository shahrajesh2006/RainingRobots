import random
import time
from player import Player 
NeelStealsSamsIdea = "y"
while NeelStealsSamsIdea== "y":
 print("Welcome to the random number game")

 players =[] #create empty list of players when the program starts

# When you create player object you can add it to the list as shown below
#Lest assume 5 players want to play the games
 count=0
 GetOnePumped = int(input("How many players are playing "))
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



 players.sort(key=lambda x: x.tries, reverse=False)
 #With the above logic if there is tie then the first player will be the winner

 print("The winner is" +players[0].name + "!!!!!")
 time.sleep(1)
 print("Here are the final results")
 
 for x in range(int(GetOnePumped)):
  players[x].PlayerResults()
 
 NeelStealsSamsIdea= input("Would you like to play again(y for yes and n for no)")
 if NeelStealsSamsIdea == "n":
    break
