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
            return "valid"
        elif self.random>guessNumber:
            return "low"
        else:
            return "high"
    
    