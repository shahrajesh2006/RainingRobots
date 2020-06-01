#importing objects for later
import random
import os
import time

class Player:#this is the class
    def __init__(self, playerName, randomNumber, numberOfAttempts):
        self.playerName = playerName
        self.randomNumber = randomNumber
        self.numberOfAttempts = numberOfAttempts
    
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
        print("Nice job " + self.playerName + "! Your number was " + str(self.randomNumber) + " and it took you " + str(self.numberOfAttempts) + " attempts to find it!")

playerName1 = input("Player 1, enter your name:")
playerName2 = input("Player 2, enter your name:")
time.sleep(1)#counts down a timer before the next step. Number in parenthesis is the count(uses import from line4)
os.system ("clear")

#this is the info for the players
Player1 = Player(playerName1, random.randrange(1,101), 0)
Player2 = Player(playerName2, random.randrange(1,101), 0)
#random import(line2) is used togenerate a number

YesnoPlayer1 = input(Player1.playerName + ", are you ready?")
if YesnoPlayer1 == "y" or "Y":
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  print("GOOOOOO!!!!!")
  time.sleep(2)
  os.system("clear")#clears the code area(uses import from line3)

RN= "y"
while RN == "y":
 x = int (input("Guess a number from 1-100: "))
 Player1.incrementNumberOfAttempts()
 result = Player1.isGuessNumberValid(x)
 if(result == "valid"):
  break#breaks 'while' loop if the guess=the number

time.sleep(2)
os.system("clear")

YesnoP2 = input(Player2.playerName + ", are you ready?")
if YesnoP2 == "y" or "Y":
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  print("GOOOOOO!!!!!")
  time.sleep(2)
  os.system("clear")

RN = "y"
while RN == "y":
 x = int (input("Guess a number from 1-100: "))
 Player2.incrementNumberOfAttempts()
 result = Player2.isGuessNumberValid(x)
 if(result == "valid"):
  break#see '55'

time.sleep(2)
os.system("clear")

print("Let's see who won!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
Player1.playerScore
Player2.playerScore

if Player1.numberOfAttempts < Player2.numberOfAttempts:
  print("The winner is " + Player1.playerName + "!")
elif Player1.numberOfAttempts > Player2.numberOfAttempts:
  print("The winner is " + Player2.playerName + "!")
elif Player1.numberOfAttempts == Player2.numberOfAttempts:
  print("It's a tie!")
  #chooses what to say based on number of attempts
