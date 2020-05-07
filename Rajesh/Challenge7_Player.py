#Here is the class Player 
class Player:
    #This is a constructor with 3 arguments
    def __init__(self, playerName, randomNumber, numberOfAttempts):  
#Below are the attributes which are assigned to the three arguments
        self.name=playerName
        self.random= randomNumber
        self.attempts= numberOfAttempts

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
     print("Ready"+self.name)
     while True:
      GuessedNumber = int (input("Guess a number between 1 and 100:"))
      self.incrementNumberOfAttempts()#increment number of attempts
      result= self.isGuessNumberValid(GuessedNumber) # compares if guessed number is equal to player's guessed number
      if(result=="valid"):
       break
     print("Great Job!")