class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
    def __add__(self,C):        # + operator overloading
        temp=Student("Both aksatth",[])
        for i in range(len(self.marks)):
            pom=[]
            for j in range(len(self.marks[0])):
                pom.append(self.marks[i][j] + C.marks[i][j])
            temp.marks.append(pom)
        return temp

S1=Student("Shubhra",[[1,2],[3,4]])
S1.display()

print()
S2=Student("Rohit",[[3,4],[5,1]])
S2.display()

print()
S3=Student("",[])
S3= S1 + S2
S3.display()