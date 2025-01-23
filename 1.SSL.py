# single linked list
#not need to think about memory management because 
#in python gurbage collection done automatically

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:   # head pointer
    def __init__(self, start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():   #checking ll is empty?
            temp=self.start
            while temp.next is not None:  #traversing
                temp=temp.next
            temp.next=n
        else:
            self.start=n   #if empty then=> start contatin new node
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp.next is not None:
            print(f'|{temp.item}|',end=' ')
            temp=temp.next
        print(f'|{temp.item}|')
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:    # if list is empty
            pass  
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:  #going 2nd last node
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None and self.start.item==data:   #if only node and match with the data
            self.start=None
        else:
            temp=self.start
            if temp.item==data:   # if the first item have to delete
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):       # for making the LL iterable
        return SLLIterator(self.start)
    # sorting of LL
    def sortLL(self):
        if not self.is_empty():
            p=self.start
            while p.next is not None:
                q=p.next
                while q is not None:
                    if p.item > q.item:
                        temp=p.item
                        p.item=q.item
                        q.item=temp
                    q=q.next
                p=p.next
class SLLIterator:   # explicitly making the LL iterable***
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:    
            raise StopIteration    #  making stop iteration by creating exceptions
        data=self.current.item 
        self.current=self.current.next
        return data
    
            
obj1=SLL()

def case2():
    num=int(input("Enter the number to add: "))
    obj1.insert_at_start(num)
def case3():
    obj1.print_list()
def case4():
    data=int(input("After which you want: "))
    val=int(input("Enter which value to enter: "))
    obj1.insert_after((obj1.search(data)),val)
def case5():
    num=int(input("Enter the item to delete: "))
    obj1.delete_item(num)
def case6():
    obj1.sortLL()
def default_case():
    exit()




def switch_case(argument):
    switch = {
        '2': case2 ,
        '3': case3 ,
        '4': case4,
        '5': case5,
        '6': case6,
        'default': "Default case code"
    }
    # Get the code corresponding to the argument from the dictionary
    # If argument not found, get default case code
    switch.get(argument, default_case)()


while True:
    print("\n\n2)add begin \n3)print\n4)Insert after\n5)Delete Item\n6)Sort in ascending order")
    ch=str(input("Enter your choice: "))
    switch_case(ch)



# driver code
myList=SLL()
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_start(40)
myList.insert_at_start(50)
myList.insert_after(myList.search(30),99)
myList.print_list()
myList.delete_item(30)
print()
myList.print_list()
print('\nPrinting by making the Object iterable: ')
for x in myList:    # first need to make our object iterable
    print(x,end=' ')
print()
