class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class SLL:
    def __init__(self):
        self.start=None
    def add_first(self,val):
        n=Node(val)
        n.link=self.start
        self.start=n
    
    def display(self):
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.link
        
obj=SLL()
obj.add_first(4)
obj.add_first(6)
obj.add_first(7)
obj.display()