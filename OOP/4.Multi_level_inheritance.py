class Person:               # Base class
    def name(self):
        print("Name...")

class Teacher(Person):       # class derived from Person
    def Qualification(self):
        print("Qualification....Ph. D must")
    
class HOD(Teacher):         #class derived from Teacher(Person -> Teacher -> HOD)
    def experince(self):
        print('Experience..... at least 15 years')
    
hod =HOD()
hod.name()
hod.Qualification()
hod.experince()