""" Write a program that has a class Person. Inherit a class Faculty from Person which also
has a class publication"""

class Person:
    def __init__(self, name, age, sex):
        self.name=name
        self.age=age
        self.sex=sex
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Sex: ",self.sex)
    
class Publications:
    def __init__(self, no_RP, no_Books, no_Art):
        self.no_RP=no_RP
        self.no_Books=no_Books
        self.no_Art=no_Art
    def display(self):
        print("Number of Research papers published: ", self.no_RP)
        print("Number of Books Published : ",self.no_Books)
        print("Number of Articles Published: ",self.no_Art)

class Faculty(Person):
    def __init__(self, name, age, sex, desig, dept, no_RP, no_Books, no_Art):
        super().__init__(name, age, sex)
        self.desig=desig
        self.dept=dept
        self.pub=Publications(no_RP, no_Books, no_Art)
    def display(self):
        super().display()
        print("Designation: ",self.desig)
        print("Department: ",self.dept)
        self.pub.display()

F = Faculty("Shubhra", 20 ,"Male", "TIC", "Computer Science", 22, 1, 3)
F.display()