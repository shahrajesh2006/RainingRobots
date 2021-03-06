import time

import os
#Here is the class Player 
class Player:
    #This is a constructor with 3 arguments
    def __init__(self, playerName, randomNumber, numberOfAttempts):  
#Below are the attributes which are assigned to the three arguments
        self.name=playerName
        self.random= randomNumber
        self.attempts= numberOfAttempts
        print("Random Number is"+str(self.random))

#this function will increment the number of attempts by 1
    def incrementNumberOfAttempts(self):
        self.attempts=self.attempts + 1
    
    #This function will compare the random number to the player's guessed number
    def isGuessNumberValid(self,guessNumber):
      if self.random==guessNumber:
        print("You guessed right!")
        return "valid"
      elif self.random>guessNumber:
        print("You guessed low!")
        return "low"
      else:
        print("You guessed high!")
        return "high"
    #This function will print the game results
    def PlayerResults(self):
       print("Player Name: " + self.name)
       print("Your random number was "  + str(self.random))
       print("Your number of attempts was " + str(self.attempts))
    
    def PlayGame(self):
       begin = input(self.name + " will play now. Are you ready? Print y if you are.")       
       if begin.lower().strip() == "y":
         print(3)
         time.sleep(1)
         print(2)
         time.sleep(1)
         print(1)
         time.sleep(1)
         os.system("clear")
       while True:
         GuessedNumber = int (input("Guess a number between 1 and 100:"))
         self.incrementNumberOfAttempts()#increment number of attempts
         result= self.isGuessNumberValid(GuessedNumber) # compares if guessed number is equal to player's guessed number
         if(result=="valid"):
                      break
#this function is used to check whether it is a exisiting player and print the welcome message




    def checkExisitingPlayer(self,player23):
        newplayer = "y" # by default the player is a new player    
        for playedbefore in range(len(player23)):
         play = player23[playedbefore].split("=")
         
         if play[0].strip() == self.name.strip():
          print("Welcome back to the random number game " + play[0] + " your score from earlier is " + str(play[1]))
          time.sleep(5)
          os.system("clear")
          newplayer = "n"
    #if it is a new player, it prints a different message
        if newplayer == "y":
         print("Welcome New Player to the random number game!!!!!!")
         time.sleep(5)
