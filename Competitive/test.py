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
        if (self.start is None):
            print("hi1")
            self.addFirst(val)
        else:
                p=self.start
                while( p.nextlink is not None):
                        print("hi")
                        p=p.nextlink
                n=node(val,p,p.nextlink)
                p.nextlink=n
    def sortDll(self):
         p=self.start
         while(p.nextlink is not None):
              q = p.nextlink
              while (q is not None):
                   if(p.data > q.data):
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                   q=q.nextlink
              p=p.nextlink

obj=DLL()
obj.addFirst(4)
obj.addFirst(5)
obj.addFirst(3)
obj.display()

obj.addLast(99)
obj.addLast(89)
obj.display()

print()
obj.sortDll()
obj.display()
    

   