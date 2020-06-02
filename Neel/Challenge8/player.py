import random 
import time
import os
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

    # this function will be used to play the games 
    def playGame(self):
      #Here is th game part of the function.
      input(self.name+" Are u ready? Press any key to continue...")
      print ("Ok lets go"+ self.name+ "!")
      while True:
        x = int (input("Guess a number between 1 and 100:"))
        self.incrementNumberOfAttempts()#increment number of attempts
        result=self.isGuessNumberValid(x)
        if(result=="valid"):
          break
    def ExistPlayer(self,sweat):
        newplayer = "y" # by default the player is a new player    
        for Skybase in range(len(sweat)):
         play = sweat[Skybase].split("=")
         
         if play[0].strip() == self.name.strip():
          print("Welcome to the Randomnuber game" + play[0] + " your score from earlier is " + str(play[1]) + " :sweat")
          time.sleep(4)
          os.system("clear")
          newplayer = "n"
    #if it is a new player, it prints a different message
        if newplayer == "y":
         print("Welcome New Player to the random number game! The goal of this game is to get the epic virctory royale.")
         time.sleep(5)