yes = 0
animals = ["dog", "cat", "mouse", "lion", "tiger", "monkey", "snake", "giraffe", "elephant", "cheetah"]
category1 = ["dog", "tiger", "giraffe", "cheetah"]
category2 = ["cat", "monkey", "elephant", "cheetah"]
category3 = ["mouse", "snake", "giraffe", "elephant", "cheetah"]
category4 = ["lion", "tiger", "monkey", "snake", "giraffe", "elephant", "cheetah"]

print(*animals, sep = "\n")# the * and \n creates a straight line down
print("Guess the Animal!")

input("Are you ready to start hit enter...")

print("CATEGORY 1")
print(*category1, sep = "\n")
print("CATEGORY 2")
print(*category2, sep = "\n")
print("CATEGORY 3")
print(*category3, sep = "\n")
print("CATEGORY 4")
print(*category4, sep = "\n")

user = input("\n" "Is your animal in category 1 - yes/no?")
if user == "yes":
    yes = yes + 1 #adds 1 to the total
user2 =  input("\n" "Is your animal in category 2 - yes/no?")
if user2 == "yes":
    yes = yes + 2 #adds 2 to total
user3 = input("\n" "Is your animal in category 3 - yes/no?")
if user3 == "yes":
    yes = yes + 3#adds 3 to total
user4 = input("\n" "Is your animal in category 4 - yes/no?") 
if user4 == "yes":
    yes = yes + 4#adds 4 to total



print("\n" "Your animal is a " + animals [yes - 1])#subtracts 1 from total so the code can associate with item from animals list
