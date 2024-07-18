class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Teacher(Person):
    def __init__(self, name, age, exp, r_area):
        super().__init__(name, age)
        self.exp=exp
        self.r_area=r_area
    def display(self):
        super().display()
        print("Experinece: ",self.exp)
        print("Research Area: ",self.r_area)

class Student(Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course=course
        self.marks=marks
    def display(self):
        super().display()
        print("Course: ",self.course)
        print("Marks: ",self.marks)

print("************* TEACHER *************")
T=Teacher("Ratul", 30, 10, "Cyber security")
T.display()

print("************* STUDENT *************")
S=Student("Shubrhajit",20,"BTech",78)
S.display()

print("T is a Teacher: ",isinstance(T,Teacher))
print("Teacher is a subclass of Person: ",issubclass(Teacher,Person))

print("Person is a subclass of Teacher: ",issubclass(Person,Teacher))