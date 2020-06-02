import os
import time

class Player:

  def __init__(self, playerName, randomNumber, numberOfAttempts):  
    self.name=playerName
    self.randomnumber= randomNumber
    self.tries= numberOfAttempts
    print("Random Number is"+str(self.randomnumber))

  def incrementNumberOfAttempts(self):
    self.tries=self.tries+1

  def isGuessNumberValid(self,guessNumber):
    if self.randomnumber==guessNumber:
      print("You guessed right!")
      return "valid"
    elif self.randomnumber>guessNumber:
      print("You guessed low!")
    else:
      print("You guessed high!")
      
  def printPlayerResults(self):
    print("Player Name: " + self.name)
    print("Your random number was "  + str(self.randomnumber))
    print("Your number of attempts was " + str(self.tries))

  def playGame(self):
    input(self.name+" are u ready? Press any key to continue:")
    os.system("clear")
    print (self.name+"'s Turn")
    while True:
      x = int (input("Guess a number between 1 and 100:"))
      self.incrementNumberOfAttempts()#increment number of attempts
      result=self.isGuessNumberValid(x)
      if(result=="valid"):
        time.sleep(2)
        os.system("clear")    
        break
        
  def checkExisitingPlayer(self,PlayeR):
    newplayer = "y" # by default the player is a new player    
    for playedbefore in range(len(PlayeR)):
        play = PlayeR[playedbefore].split("=")
            
        if play[0].strip() == self.name.strip():
            print("Welcome Back " + play[0] + " | Your Previous Score = " + str(play[1]))
            time.sleep(5)
            os.system("clear")
            newplayer = "n"
        
    if newplayer == "y":
        print("Welcome New Player")
        time.sleep(5)

            
