#Program to overload + operator on a complex object

class Complex:
    def __init__(self):
        self.real=0
        self.imag=0
    def setvalue(self, real, imag):
        self.real=real
        self.imag=imag
    def __add__(self,C):     # + opearator overloading, the argument are important
        temp=Complex()
        temp.real=self.real + C.real
        temp.imag=self.imag + C.imag
        return temp
    def display(self):
        print('( ',self.real," + ",self.imag," i)")

c1=Complex()
c1.setvalue(1,2)
c2=Complex()
c2.setvalue(3,4)

c3=Complex()
c3=c1+c2
print("Result: ")
c3.display()