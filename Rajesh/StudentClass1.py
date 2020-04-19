class Student:
    name = "name"
    grade="grade"

    def printStudentInformation(self):
        print("Student Information- Name:"+self.name+" Grade: "+self.grade)
      
vir = Student()
vir.name="Vir"
vir.grade="7th"

vihaan = Student()
vihaan.name="Vihaan"
vihaan.grade="6th"

aarav = Student()
aarav.name="Aarav"
aarav.grade="7th"

samhith = Student()
samhith.name="Samhith"
samhith.grade="6th"

neel = Student()
neel.name="Neel"
neel.grade="7th"

vir.printStudentInformation()
vihaan.printStudentInformation()
aarav.printStudentInformation()
samhith.printStudentInformation()
neel.printStudentInformation()
