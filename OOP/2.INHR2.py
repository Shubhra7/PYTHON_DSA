class Base1(object):
    def __init__(self):
        print("Base1 class")
        super(Base1, self).__init__()

class Base2(object):
    def __init__(self):
        print("Base2 class")

class Derived(Base1, Base2):
    pass

D=Derived()

