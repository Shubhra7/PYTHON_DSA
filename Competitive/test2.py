class Node:
    def __init__(self,data=None,prevlink=None,nextlink=None):
        self.data = data
        self.prevlink = prevlink
        self.nextlink = nextlink

class DLL:
    def __init__(self):
        self.start = None

    def isEmpty(self):
        if (self.start is None):
            return True
        else:
            return False
        
    def add_First(self,data):
        if(self.isEmpty()):
            n=Node(data)
            self.start=n
        else:
            n=Node(data)
            n.nextlink=self.start
            self.start=n
    
    def display(self):
        if(not self.isEmpty()):
            p=self.start
            while(p is not None):
                print(p.data,end=" ")
                p=p.nextlink
    
    def add_last(self,data):
        if(self.isEmpty()):
            self.add_First(data)
        else:
            p=self.start
            while( p.nextlink is not None):
                p = p.nextlink
            print(p.data)
            n=Node(data)
            n.prevlink=p
            p.nextlink=n
    
    def add_after(self,val,data):
        if(self.isEmpty()):
            print("Empty list")
        else:
            p=self.start
            while (p is not None):
                if(p.data == val):
                    n=Node(data)
                    n.prevlink = p
                    n.nextlink = p.nextlink
                    p.nextlink = n
                    break
                p=p.nextlink
            else:
                print("Not found!!")
    
    def add_before(self,val,data):
        if(self.isEmpty()):
            print("Empty List!!")
        elif (self.start.data == val):
            self.add_First(data)
        else:
            p=self.start
            while(p.nextlink is not None):
                if(p.nextlink.data == val):
                    n=Node(data)
                    n.prevlink=p
                    n.nextlink=p.nextlink
                    p.nextlink.prevlink = n
                    p.nextlink = n
                    break
                p=p.nextlink
            else:
                print("Not Found!!")
    
    def sort_ll(self):
        p=self.start
        while (p.nextlink is not None):
            q=p.nextlink
            while (q is not None):
                if(p.data > q.data):
                    temp=p.data
                    p.data=q.data
                    q.data=temp
                q=q.nextlink
            p = p.nextlink


            

obj= DLL()
obj.add_First(3)
obj.add_First(10)
obj.add_last(33)
obj.add_last(69)

obj.add_after(10,108)

obj.add_before(69,1007)

print("The printed list is: ",end="")
obj.display()

print()
obj.sort_ll()
print("The sorted printed list is: ",end="")
obj.display()



        
        