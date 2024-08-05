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
    def isEmpty(self):
        if self.start is None:
            return True
        else:
            return False
    def add_end(self,val):
        if not self.isEmpty():
            p=self.start
            while p.link is not None:
                p=p.link
            n=Node(val)
            p.link=n
        else:
            self.add_beg(val)
    def add_after(self,data,val):
        if not self.isEmpty():
            p=self.start
            while ( p is not None and p.data!=data):
                p=p.link
            if p is not None:
                n=Node(val,p.link)
                p.link=n

        

obj=SLL()
obj.add_beg(4)
obj.add_beg(5)
obj.add_beg(7)

obj.add_end(1)
obj.add_end(10)
obj.add_end(77)

obj.add_after(77,99)
obj.display()


