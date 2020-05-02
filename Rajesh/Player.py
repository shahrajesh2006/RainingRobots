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
