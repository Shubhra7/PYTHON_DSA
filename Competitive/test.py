class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class SLL:
    def __init__(self):
        self.start=None
    def add_beg(self,val):
        n=Node(val,self.start)
        self.start=n
    def display(self):
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.link
        print()

obj=SLL()
obj.add_beg(4)
obj.add_beg(5)
obj.add_beg(7)
obj.display()