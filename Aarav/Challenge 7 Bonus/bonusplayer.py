class Player:
  def __init__(self, playerName, randomNumber, numberOfAttempts):
    self.name = playerName
    self.number = randomNumber
    self.attempts = numberOfAttempts

  def incrementNumberOfAttempts(self):
    self.attempts = self.attempts + 1

  def isGuessNumberValid(self, guessNumber):
      if self.number == guessNumber: 
        print("You guessed RIGHT!")
        return "correct"
      elif self.number > guessNumber:
        print("You guessed low.")
        return "low"
      else:
        print("You guessed high.")
        return "high"

  def playGame(self):
    print("Now " + self.name + " will play!")
    while True:
      guessNumber = int(input("Guess a number between 1 and 100: ")) 
      self.incrementNumberOfAttempts()
      cow = self.isGuessNumberValid(guessNumber)
      if cow == "correct":
        break

  def playerResults(self):
    print("Name: " + self.name)
    print("You took " + str(self.attempts) + " tries to guess your number.")

  def isitaTie(self,players):
    if players[0].attempts==players[1].attempts:
        return True
    else:
        return False
