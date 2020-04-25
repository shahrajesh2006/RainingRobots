class Student:

    #Constructor is nothing but a helper function to create object
    def __init__(self,name,grade,hobby):
        self.name=name
        self.grade=grade
        self.hobby=hobby

    #Function to print student information
    def printStudentInformation(self):
        print("Student Information- Name:"+self.name+" Grade: "+self.grade)

    def studentHobby(self):
        return self.hobby

vir = Student("Vir","7th","gaming")

vihaan = Student("Vihaan","6th","golf")

aarav = Student("Aarav","7th","rubik")

samhith = Student("Samhith","6th","maps")

neel = Student("Neel","7th","crankin90s")

hansika = Student("Hansika","VT Sophomore","watching tv")



vir.printStudentInformation()
vihaan.printStudentInformation()
aarav.printStudentInformation()
samhith.printStudentInformation()
neel.printStudentInformation()
hansika.printStudentInformation()

student=input("Type Student Name to find Hobby:")

hobby="Not found"

if(vir.name==student):
  hobby=vir.studentHobby()
elif(vihaan.name==student):
  hobby=vihaan.studentHobby()
elif(aarav.name==student):
  hobby=aarav.studentHobby()
elif(samhith.name==student):
  hobby=samhith.studentHobby()
elif(neel.name==student):
  hobby=neel.studentHobby()
elif(hansika.name==student):
  hobby=hansika.studentHobby()

print("Hobby is "+hobby)

