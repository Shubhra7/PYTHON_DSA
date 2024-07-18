class Node:
    def __init__(self,item=None,priority=None,next=None) -> None:
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self) -> None:
        self.start=None
        self.item_count=0
    def push(self,data,priority):
        n=Node(data,priority)
        if self.start is None or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority <= priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1
    def is_empty(self):
        return self.start==None
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
    def size(self):
        return self.item_count
    
p=PriorityQueue()
p.push("Amit",3)
p.push("Amitra",1)
p.push("Bubai",7)
p.push("Kalu",6)


while not p.is_empty():
    print(p.pop())