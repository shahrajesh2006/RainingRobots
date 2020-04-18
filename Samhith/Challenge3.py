import random #module to random generator
ui = "y"
randomnumber = random.randrange(1,101)# this will generate random number from 1-100
while ui == "y":
  #randomnumber = (random.randrange(1,101))
  playersguess = int ( input("Guess a number between 1-100"))#convert input to int type
  if playersguess == randomnumber:
    print("You guessed correct!")
  elif playersguess > randomnumber:
   print("You guessed high!")
  elif playersguess < randomnumber:
    print("You guessed low!")   
  
  ui = (input("Do you want to play again? If yes, type y. If n, type no."))
