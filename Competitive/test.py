#  double Linked List 

class node:
    def __init__(self,data=None,prevlink=None,nextlink=None):
        self.data = data
        self.prevlink = prevlink
        self.nextlink = nextlink

class DLL:
    def __init__(self) -> None:
        self.start = None
    def addFirst(self,val):
        n=node(val,None,self.start)
        self.start=n
    def display(self):
        print("The double linked list is:",end=" ")
        p=self.start
        while( p is not None):
            print(p.data,end=" ")
            p=p.nextlink
    def addLast(self,val):
        

obj=DLL()
obj.addFirst(4)
obj.addFirst(3)
obj.addFirst(5)
obj.display()
    

   