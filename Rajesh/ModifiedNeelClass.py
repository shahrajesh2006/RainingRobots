class Robot:
#This is a constructor which helped make the code smaller and easier
    def __init__(self, Name, Color, Weight):  
#Each of these are setting one of the attribute to the given robot
        self.name=Name
        self.color=Color
        self.weight=Weight
 #Here are my functions that are the way the words are written out
    def introduce_self(self,number):
        print("Hi my name is " + self.name)
        print("Value of number is " + str(number))
    
    def introduce_Color(self):
        print("Hi my color is " + self.color)
    
    def introduce_Weight(self):
        print("Hi my weight is " + self.weight)
    
    def compareWeight(self,wt):
        if(self.weight==wt):
          return "SAME"
        elif(self.weight<wt):
          return "LOW"
        else:
          return "HIGH"
          
#Here is all of the data. Also this is in the form the constructor is in which is above.

r1 = Robot("neel", "Green", "30")
r2 = Robot("Tom", "blue", "40")
#Here I am calling all my functions in an easy and reliable way.
print("Robot 1:")
r1.introduce_self(10)
r1.introduce_Color()
r1.introduce_Weight()

var compareWeight1=r1.compareWeight(30)

print("Robot 2:")
r2.introduce_self(8)
r2.introduce_Color()
r2.introduce_Weight()


#r1.name = "Neel" 
#r1.color = "Green"
#r1.weight = 30  
#r1.introduce_self()  
