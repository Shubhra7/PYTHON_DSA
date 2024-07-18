class PriorityQueue:
    def __init__(self) -> None:
        self.items=[]
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1] >= priority:
            index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty!")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
    def print1(self):
        print(self.items)
    
p=PriorityQueue()
p.push("Amit",3)
p.push("Amitra",1)
p.push("Bubai",7)
p.push("Kalu",6)
p.print1()

while not p.is_empty():
    print(p.pop())

p.print1()