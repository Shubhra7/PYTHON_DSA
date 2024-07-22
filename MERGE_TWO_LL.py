class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class LinkedList:
    def __init__(self):
        self.start=None
    def add_first(self,data):
        n=Node(data,self.start)
        self.start=n
    def display(self):
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.link

def merge_LL(LL1,LL2):
    p=LL1.start
    while p.link is not None:
        p=p.link
    p.link=LL2.start
        

LL1=LinkedList()
LL1.add_first(3)
LL1.add_first(6)
LL1.add_first(1)
LL1.add_first(7)
LL1.display()
print()

LL2=LinkedList()
LL2.add_first(4)
LL2.add_first(2)
LL2.add_first(10)
LL2.display()

merge_LL(LL1,LL2)
print("\nAfter merging the LinkedList will be: ")
LL1.display()