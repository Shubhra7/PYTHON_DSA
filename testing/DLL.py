class Node:
    def __init__(self,data=None,prevlink=None,nextlink=None):
        self.data=data
        self.prevlink=prevlink
        self.nextlink=nextlink

class DLL:
    def __init__(self):
        self.start=None
    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False

    def add_beg(self,data):
        n=Node(data)
        n.nextlink=self.start
        if self.start is not None:
            self.start.prevlink=n
        self.start=n
    
    def display(self):
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.nextlink

obj=DLL()
obj.add_beg(4)
obj.add_beg(6)
obj.add_beg(1)
obj.display()
