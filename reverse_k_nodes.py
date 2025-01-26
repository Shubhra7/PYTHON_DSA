class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:   # head pointer
    def __init__(self, start=None):
        self.start=start
    def rev_k_ll(self,k):
        
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def print_list(self):
        temp=self.start
        while temp.next is not None:
            print(f'|{temp.item}|',end=' ')
            temp=temp.next
        print(f'|{temp.item}|')

obj=SLL()
obj.insert_at_start(5)
obj.insert_at_start(4)
obj.insert_at_start(3)
obj.insert_at_start(2)
obj.insert_at_start(1)
print("List is before k reverse: ")
obj.print_list()
obj.rev_k_ll(2)
obj.print_list(obj)