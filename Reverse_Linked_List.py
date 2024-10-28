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
    def reverseList(self,head):
        if head is None or head.next is None:
            return head
        
        # Reverse the rest list
        rest = self.reverseList(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest

obj = LinkedList()
obj.push(3)
obj.push(4)
obj.push(45)

print("The primary Linekd List is: ")
print(obj)

obj.head = obj.reverseList(obj.head)

print("The reversed Linked list is: ")
print(obj)
        
