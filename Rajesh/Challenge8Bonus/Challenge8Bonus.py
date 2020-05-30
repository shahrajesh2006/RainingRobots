import random 
import os
import time
from player import Player


# Using readlines() 
file1 = open('Rajesh/bestscore.txt', 'r') 
Lines = file1.readlines() # this list of all the lines from the file

# Strips the newline character 
for line in Lines: 
	print(line.strip()) 

#Before we start the game lest load the existing player scores in a list

# Using readlines() 
file2 = open('Rajesh/players.txt', 'r') 
players_file = file2.readlines() # list of all lines from the file

#Line 1-2 are the random number and operating system module 
numberofpeopleplaying = input("How many people are playing? The max is 10 players.")
time.sleep(1)
os.system("clear")


#Here is the object with three arguments more comments
#more comments please
players = []

peopleplayingvalue = 0

while peopleplayingvalue < int(numberofpeopleplaying):
 playersname = input("Player" + str(peopleplayingvalue + 1) + " what is your name or nickname")
 # Now see if this player is new player or existing player
 existing_player="n" # assume he is not existing player
 for n in range(len(players_file)): # Step 1 loop through the lines
    y=players_file[n].split("=") # Step 2 split the line
    #print("splitting Name"+y[0])
    if y[0]==playersname:# if name is in the file then existing player
       print("Welcome back "+y[0]+"your previous score was" + y[1])
       existing_player="y"

# If its a new player print different message
 if existing_player=="n":
    print("Welcome new player "+playersname)

 NewPerson = Player(playersname, random.randrange(1,101), 0)
 players.append(NewPerson)
 print ("New player created..."+players[peopleplayingvalue].name)
 peopleplayingvalue=peopleplayingvalue+1


# players.append(NewPerson)
# peopleplayingvalue = peopleplayingvalue + 1
time.sleep(1)
os.system("clear")
   

peopleplayingvalue = 0
while peopleplayingvalue < int(numberofpeopleplaying):
  players[peopleplayingvalue].PlayGame()
  print ("after game")
  peopleplayingvalue = peopleplayingvalue + 1


#This ask player 2 if they are ready
print("Are")
time.sleep(1)
print("you")
time.sleep(1)
print("ready")
time.sleep(1)
print("to see")
time.sleep(1)
print("who")
time.sleep(1)
print("won?")
ready = input("Print y to continue")

if ready.lower().strip() =="y": 
  print("Then lets... see... who... wonnnnnnnnn!")
time.sleep(1)
os.system ("clear") #Clears screen


WinningPlayer = players[0]# For now assume first player won
print("For now the winning player is "+WinningPlayer.name)
print(WinningPlayer)


peopleplayingvalue = 0
while peopleplayingvalue < int (numberofpeopleplaying):
  time.sleep(1)
  print("looping for the player"+players[peopleplayingvalue].name)
  if players[peopleplayingvalue].attempts < WinningPlayer.attempts:
   WinningPlayer = players[peopleplayingvalue]#found a better player so switch
   print("Found the new winning player is "+WinningPlayer.name)
  else:
    print("Winning player is still the same "+WinningPlayer.name)
  peopleplayingvalue = peopleplayingvalue + 1

#With the above logic if there is tie then the first player will be the winner
  

print("The winner is" + WinningPlayer.name)
file1 = open('Rajesh/bestscore.txt', 'w') 
file1.writelines("Winner of the last game:"+ WinningPlayer.name+"\n")
file1.writelines("Best Score for the last game:"+ str(WinningPlayer.attempts)+"\n")
file1.close()

#Now lets write the players.txt

file2 = open('Rajesh/players.txt', 'w')

for n in range(int(numberofpeopleplaying)):
    file2.writelines(players[n].name+"="+str(players[n].attempts)+"\n")

file2.close()

