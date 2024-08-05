<<<<<<< HEAD
class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

class SLL:
    def __init__(self):
        self.start=None
    def add_beg(self,val):
        n=Node(val,self.start)
        self.start=n
    def display(self):
        p=self.start
        while p is not None:
            print(p.data,end=" ")
            p=p.link
        print()

obj=SLL()
obj.add_beg(4)
obj.add_beg(5)
obj.add_beg(7)
obj.display()

def maxSubarraySum(arr):
    cur_max=arr[0]
    ans=arr[0]
    for i in range(1,len(arr)):
        cur_max = max(arr[i], arr[i]+cur_max)
        ans=max(ans,cur_max)
    return ans



arr=[5,4,-1,7,8]
print(maxSubarraySum(arr))
>>>>>>> 73fbde2caaac984a150a153786b74d72c55c1f65
