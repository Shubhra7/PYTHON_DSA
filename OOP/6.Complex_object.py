class One:
    def set(self,var):
        self.var=var
    def get(self):
        return self.var

class Two:
    def __init__(self,var):
        self.o=One()        # object of class One is created
    #method of class One is invoked using its object in class TWO
        self.o.set(var)
    def show(self):
        print("Number = ",self.o.get())

T=Two(100)
T.show()