class Base1(object):            # First Base class
    def __init__(self) -> None:
        super(Base1,self).__init__()
        print("Base1 Class")

class Base2(object):        # Second Base Class
    def __init__(self) -> None:
        super(Base2, self).__init__()
        print("Base2 Class")
    
class Derived(Base1, Base2):      #Derived class Derived from Base1 and Base2
    def __init__(self) -> None:
        super().__init__()
        print("Derived Class")

D=Derived()