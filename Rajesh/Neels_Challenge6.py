import random
import os

print("Welcome to the random number game")


#Here is my my class with my constructor and functions
class Player:
    #This is a constructor
    def __init__(self, playerName, randomNumber, numberOfAttempts):  
#Each of these are setting one of the attribute to the given robot
        self.name=playerName
        self.randomnumber= randomNumber
        self.tries= numberOfAttempts

#this function will increment the number of attempts by 1
    def incrementNumberOfAttempts(self):
        self.tries=self.tries+1

    def isGuessNumberValid(self,guessNumber):
      if self.randomnumber==guessNumber:
        print("You guessed right!")
        return "valid"
      elif self.randomnumber>guessNumber:
        print("You guessed low!")
        return "low"
      else:
        print("You guessed high!")
        return "high"

    def printPlayerResults(self):
       print("Player Name: " + self.name)
       print("Your random number was "  + str(self.randomnumber))
       print("Your number of attempts was " + str(self.tries))

#Here is the way I get the name
Player1name= input("Player 1, what would you like your name to be:")
P1 = Player(Player1name, random.randrange(1,101), 0)


Player2name= input("Player 2, what would you like your name to be:")
P2 = Player(Player2name,  random.randrange(1,101), 0)

os.system ("clear")



#Here is th game part of the function.
while True:
 x = int (input("Guess a number between 1 and 100:"))
 P1.incrementNumberOfAttempts()#increment number of attempts
 result=P1.isGuessNumberValid(x)
 if(result=="valid"):
   break


#This ask player 2 if they are ready
YesnoP1 = input("Player 2 ready?")
if YesnoP1 =="y" or "Y":
 print ("Ok lets go")
os.system ("clear")

#Here is the game for player 2 
while True:
 x = int (input("Guess a number between 1 and 100:"))
 P2.incrementNumberOfAttempts()#increment number of attempts
 result=P2.isGuessNumberValid(x)
 if(result=="valid"):
   break



#Here I am asking to say if they are ready for the winner
YesnoP2 = input("Are we ready to see who won(type y to continue)?")
if YesnoP2 =="y" or "Y":
 print ("Drumroll please")
os.system ("clear")

#Here I am writing the winner
if P1.tries < P2.tries:
  print("The winner is " + Player1name)
elif P1.tries > P2.tries:
  print("The winner is " + Player2name)
elif P1.tries == P1.tries:
  print("Its a tie")
print("----------------------------------")

#Here I am writing the final stats
print("Here are the final results")
P1.printPlayerResults()
P2.printPlayerResults()
