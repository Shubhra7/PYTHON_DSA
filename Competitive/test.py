class Node:
    def __init__(self,data=None,prevlink=None,nextlink=None):
        self.data=data
        self.prevlink=prevlink
        self.nextlink=nextlink

class DLL:
    def __init__(self) -> None:
        self.start = None
    def add_first(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            self.start.prevlink = n
            n.nextlink=self.start
            self.start=n
    def display(self):
        p=self.start
        print("The Linked list is: ")
        while p is not None:
            print("|",p.data,"|",end=" -> ")
            p=p.nextlink

obj = DLL()
obj.add_first(3)
obj.add_first(4)
obj.add_first(6)

obj.display()        