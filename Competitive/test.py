class Node:
    def __init__(self,data=None,prevlink=None,nextlink=None):
        self.data=data
        self.prevlink=prevlink
        self.nextlink=nextlink

class DLL:
    def __init__(self) -> None:
        self.start = None
    def add_last(self,data):
        if self.start is None:
            self.add_first(data)
            return
        n=Node(data)
        p=self.start
        while p.nextlink is not None:
            p=p.nextlink
        p.nextlink=n
        n.prevlink=p
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
        print()
        print("The Linked list is: ")
        while p is not None:
            print("|",p.data,"|",end=" -> ")
            p=p.nextlink
    def reverse(self):
        l=self.start
        p=l.nextlink
        while p is not None:
            temp1=l.nextlink
            l.nextlink=l.prevlink
            l.prevlink=temp1
            l=p
            p=l.nextlink
        temp1=l.nextlink
        l.nextlink=l.prevlink
        l.prevlink=temp1
        self.start=l
    def sortLL(self):
        p=self.start
        while p is not None:
            q=p.nextlink
            while q is not None:
                if (p.data > q.data):
                    temp=p.data
                    p.data=q.data
                    q.data=temp
                q=q.nextlink
            p=p.nextlink



obj = DLL()

obj.add_first(12)
obj.add_first(45)
obj.add_first(6)
# obj.add_last(4555)
obj.add_first(3)
obj.add_first(4)
obj.add_last(499)

obj.display()  
obj.sortLL()

obj.display()



# obj.reverse()

# obj.display()