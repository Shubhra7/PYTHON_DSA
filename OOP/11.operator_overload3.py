class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
    def __add__(self,C):        # + operator overloading
        temp=Student("Both aksatth",[])
        for i in range(len(C.marks)):
            temp.marks.append(self.marks[i] + C.marks[i])
        return temp

S1=Student("Shubhra",[4, 6,7,8])
S1.display()

print()
S2=Student("Rohit",[1,2,1,2])
S2.display()

print()
S3=Student("",[])
S3= S1 + S2
S3.display()