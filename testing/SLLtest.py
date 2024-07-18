# Single linked list code

class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class SLL:
    def __init__(self):
        self.start=None

    def add_first(self,data):
        n=Node(data,self.start)
        self.start=n

    def add_last(self,data):
        p=self.start
        while p.link is not None:
            p=p.link
        n=Node(data)
        p.link=n
    
    def add_after(self,val,data):
        p=self.start
        while p is not None and p.data!=val:
            p=p.link
        if p is None:
            print("Not present your value is the linked list")
        else:
            n=Node(data,p.link)
            p.link=n

    def add_before(self,val,data):
        p=self.start
        if p.data == val:
            n=Node(data,self.start)
            self.start=n
        else:
            while p.link is not None and p.link.data!=val:
                p=p.link
            n=Node(data,p.link)
            p.link=n
    
    def delete_item(self,val):
        p=self.start
        if self.start is None:
            print("Empty Linked List")
        elif p.data == val:
            self.start=self.start.link
        else:
            while p.link is not None and p.link.data!= val:
                p=p.link
            if p.link is None:
                print("Not present")
            else:
                p.link=p.link.link


    def display(self):
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.link
        print()

    def sortLL(self):
        p=self.start
        while(p.link is not None):
            q=p.link
            while(q is not None):
                if p.data > q.data:
                    temp=p.data
                    p.data=q.data
                    q.data=temp
                q=q.link
            p=p.link

obj=SLL()
obj.add_first(3)
obj.add_first(4)
obj.add_first(5)

obj.add_last(99)

obj.add_after(99,77)

obj.add_before(99,1)

obj.display()

obj.delete_item(3)

# obj.add_first(3)
# obj.add_first(4)
# obj.add_first(5)
# obj.add_first(6)

obj.display()

obj.sortLL()

obj.display()
