class Node:
    def __init__(self,data=None,prevlink=None,nextlink=None):
        self.data = data
        self.prevlink = prevlink
        self.nextlink = nextlink

class DLL:
    def __init__(self):
        self.start = None

    def isEmpty(self):
        if (self.start is None):
            return True
        else:
            return False
        
    def add_First(self,data):
        if(self.isEmpty()):
            n=Node(data)
            self.start=n
        else:
            n=Node(data)
            n.nextlink=self.start
            self.start=n
    
    def display(self):
        if(not self.isEmpty()):
            p=self.start
            while(p is not None):
                print(p.data,end=" ")
                p=p.nextlink

obj= DLL()
obj.add_First(3)
obj.add_First(10)

obj.display()



        
        