import time
import os

class Player:#this is the class
    def __init__(self, playerName, randomNumber, numberOfAttempts):
        self.playerName = playerName
        self.randomNumber = randomNumber
        self.numberOfAttempts = numberOfAttempts
        print(self.randomNumber)

    def incrementNumberOfAttempts(self):#this counts attempts
          self.numberOfAttempts = self.numberOfAttempts + 1

    def isGuessNumberValid(self, guessNumber):#checks if guess = number
        if self.randomNumber == guessNumber:
          print("Good Job!")
          return "valid"
        elif self.randomNumber > guessNumber:
          print("Too low!")
          return "low"
        elif self.randomNumber < guessNumber:
          print("Too high!")
          return "high"
          #these 3 tell the user wether their guess is correct, low, or high

    def playerScore(self):#tells player their score
        print("You're random number was " + self.randomNumber + ". It took you the least amount of attempts, with an astounding " + self.numberOfAttempts + " attempts! Congratulations!")
        return"and..."

    def playGame(self):
      start = input(self.playerName + ", are you ready?")
      if start.lower().strip() == "y" or "Y":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GOOOOOO!!!!!")
        time.sleep(2)
        os.system("clear")#clears the code area(uses import from line3)

      while True:
        guessedNumber = int (input("Guess a number from 1-100: "))
        self.incrementNumberOfAttempts()
        result = self.isGuessNumberValid(guessedNumber)#checks if guess=number
        if(result == "valid"):
          break#breaks 'while' loop if the guess=the number