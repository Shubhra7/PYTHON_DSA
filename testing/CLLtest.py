class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class CLL:
    def __init__(self):
        self.last=None
    def is_empty(self):
        if self.last is None:
            return True
        else:
            return False
    def add_first(self,data):
        if self.is_empty():
            n=Node(data)
            n.link=n
            self.last=n
        else:
            n=Node(data,self.last.link)
            self.last.link=n
    def display(self):
        p=self.last.link
        while p != self.last:
            print(p.data,end=" ")
            p=p.link
        print(p.data)
    

obj=CLL()

obj.add_first(4)
obj.add_first(5)
obj.add_first(9)

obj.display()