class Student:

    #Constructor is nothing but a helper function to create object
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    #Function to print student information
    def printStudentInformation(self):
        print("Student Information- Name:"+self.name+" Grade: "+self.grade)


vir = Student("Vir","7th")

vihaan = Student("Vihaan","6th")

aarav = Student("Aarav","7th")

samhith = Student("Samhith","6th")

neel = Student("Neel","7th")


vir.printStudentInformation()
vihaan.printStudentInformation()
aarav.printStudentInformation()
samhith.printStudentInformation()
neel.printStudentInformation()
