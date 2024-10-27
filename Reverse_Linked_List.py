class Node:
    def __init__(self,val=None,next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def push(self,data):
        n = Node(data,self.head)
        self.head = n
    def __str__(self) -> str:
        llprint=""
        p=self.head
        while p is not None:
            # print(p.val,end=" ")
            llprint += str(p.val)+ " "
            p = p.next
        return llprint

obj = LinkedList()
obj.push(3)
obj.push(4)
obj.push(45)

print(obj)
        
