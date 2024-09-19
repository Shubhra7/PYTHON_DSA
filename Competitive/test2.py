class Node:
    def __init__(self,data=None, link=None):
        self.data=data
        self.link=link

class SLL:
    def __init__(self):
        self.start = None
    def add_first(self,data):
        n=Node(data)
        n.link=self.start
        self.start=n
        print("hi")
    def display(self):
        p=self.start
        while p is not None:
            print("|",p.data,"|",end=" -> ")
            p=p.link
    def reverse(self):
        l=None
        q=self.start
        n=q.link
        while q.link is not None:
            q.link=l
            l=q
            q=n
            n=q.link
        q.link=l
        self.start=q

obj=SLL()
obj.add_first(4)
obj.add_first(3)
obj.add_first(5)
obj.add_first(52)

obj.display()
obj.reverse()
print()
obj.display()
        