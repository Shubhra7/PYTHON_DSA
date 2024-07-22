class pri_queue:
    def __init__(self):
        self.items=[]
    def push(self,item,prio):
        i=0
        while i< len(self.items) and prio <= self.items[i][1]:
            i+=1
        self.items.insert(i,[item,prio])
    def print(self):
        print(self.items)

obj=pri_queue()
obj.push("kalu",1)
obj.push("golu",3)
obj.push("Lalu",2)

obj.print()
