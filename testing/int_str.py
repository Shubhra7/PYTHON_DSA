class node1:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class node2:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class LL:
    def __init__(self):
        self.start=None
    def add_str_node(self,data):
        n=node2(data,self.start)
        self.start=n
    def add_int_node(self, data):
        n=node1(data,self.start)
        self.start=n

    def display(self):
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.link

obj=LL()
obj.add_str_node("kalu")
obj.add_str_node("golu")
obj.add_str_node(4)
obj.add_str_node(5)
obj.display()
print()
