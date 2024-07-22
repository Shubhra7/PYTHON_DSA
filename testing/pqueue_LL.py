class Node:
    def __init__(self,data=None,prio=None,link=None):
        self.data=data
        self.prio=prio
        self.link=link

class pqueue:
    def __init__(self):
        self.start=None
    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False
    def add_beg(self,n):
        n.link=self.start
        self.start=n
    def push(self,data,prio):
        n=Node(data,prio)
        if not self.is_empty():
            if self.start.prio < prio:
                self.add_beg(n)
            else:
                p=self.start
                while p.link is not None and p.link.prio > prio:
                    p=p.link
                n.link=p.link
                p.link=n
        else:
            self.start=n
            
    
    def display(self):
        print()
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.link
    
    def peek(self):
        return self.start.data

obj=pqueue()
obj.push(4,4)   #4
obj.display()

obj.push(5,6)   #5 4
obj.display()

obj.push(99,3)   #5 4 99
obj.display()

obj.push(45,7)    #45 5 4 99
obj.display()

obj.push(105,2)    #45 5 4 99 105
obj.display()

print("\n\nThe top value is: ",obj.peek()
)
    