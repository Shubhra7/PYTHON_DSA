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
    def add_last(self,data):
        if self.is_empty():
            self.add_first(data)
        else:
            n=Node(data,self.last.link)
            self.last.link=n
            self.last=n
    def insert_after(self,val,data):
        if self.is_empty():
            self.add_first(data)
        else:
            if self.last.data == val:
                self.add_last(data)
            else:
                p=self.last.link
                while p.data!= val and p!=self.last:
                    p=p.link
                if p == self.last:
                    print("Not present!!")
                else:
                    n=Node(data,p.link)
                    p.link=n
    def sortCLL(self):
        p=self.last.link
        while p != self.last:
            q=p.link
            while q != self.last.link:
                if p.data > q.data:
                    temp=p.data
                    p.data=q.data
                    q.data=temp
                q=q.link
            p=p.link


    

obj=CLL()

obj.add_first(4)
obj.add_first(5)
obj.add_first(9)

obj.display()

print()
obj.add_last(99)
obj.add_last(77)
obj.display()

obj.insert_after(9,101)
obj.display()

print("After sorting:")
obj.sortCLL()
obj.display()


