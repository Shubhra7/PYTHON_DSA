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
    
    def search(self,data):
        p=self.start
        while p is not None:
            if p.data == data:
                return p
            p=p.nextlink
        return None
        
    
    def add_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp,temp.nextlink)
            if temp.nextlink is not None:
                temp.nextlink.prevlink=n
            temp.nextlink=n
        else:
            print("not present your data")

    
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

print()
obj.add_after(obj.search(4),99)
obj.display()
