class Robot:
    def __init__(self, Name, Color, Weight):
      self.name = Name
      self.color = Color
      self.weight = Weight # lines 2-5 are a constructor used to make the coding easier

    def introduce_self(self):
        print("My name is " + self.name + ".")
        print("I am " + self.color + ".")

#r1 = Robot()
#r1.name = "Tom"
#r1.color = "red"
#r1.weight = 30

#r2 = Robot()
#r2.name = "Jerry"
#r2.color = "blue"
#r2.weight = 40
# lines 10-18 are also ways you can code a class

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
# 22-23 go along with the constructor

r1.introduce_self()
r2.introduce_self()
