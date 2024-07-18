class Book:
    def __init__(self) -> None:
        self.title=" "
        self.publisher=''
        self.price=0
    
    def set(self, title, publisher, price):
        self.title=title
        self.publisher=publisher
        self.price=price
    
    def display(self):
        print("Title: ",self.title)
        print("Publisher: ",self.publisher)
        print("Price: ",self.price)
    
    def __gt__(self,B):         # overloading the > operator
        if self.price > B.price:
            return True
        else:
            return False


B1=Book()
B1.set("OOP with C++", "Oxford university Press", 525)
B2=Book()
B2.set("Let us C++", "BPB", 300)

if B1 > B2:
    print("The Book has more knowledge so I will Buy")
    B1.display()
