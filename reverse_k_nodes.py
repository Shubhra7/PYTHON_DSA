# https://leetcode.com/problems/reverse-nodes-in-k-group/
# https://www.youtube.com/watch?v=lIar1skcQYI

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:   # head pointer
    def __init__(self, start=None):
        self.start=start
    def kth_node_find(self,temp,k):
        k-=1
        while temp is not None and k>0:
            k-=1
            temp=temp.next
        return temp
    
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next=None
        return rest
    
    def rev_k_ll(self,k):
        temp=self.start
        prevLast=None
        while temp is not None:
            kthNode=self.kth_node_find(temp,k)
            # print(kthNode)
            if kthNode is None:
                if prevLast:
                    prevLast.next=temp
                    break
            nextNode=kthNode.next
            kthNode.next=None
            newhead=self.reverse(temp)
            if temp==self.start:
                self.start=newhead
            else:
                prevLast.next=newhead
            prevLast=temp
            temp=nextNode
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
# obj.rev_k_ll(2)   #[2,1,4,3,5]
obj.rev_k_ll(3)     #[3,2,1,4,5]
obj.print_list()