# Python program to merge K sorted linked lists
import heapq
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to merge two sorted lists.

# Function to merge K sorted linked lists
def mergeKLists(arr):
    if len(arr)==0:
        return
    min_heap=[]
    for index,node in enumerate(arr):
        if node:
            heapq.heappush(min_heap,(node.data,index,node))
    dummy=Node(0)
    cur=dummy
    while min_heap:
        node_val,index,smallest_node=heapq.heappop(min_heap)
        cur.next=smallest_node
        cur=cur.next
        if smallest_node.next:
            heapq.heappush(min_heap,(smallest_node.next.data,index,smallest_node.next))
    return dummy.next

    

def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next

if __name__ == "__main__":
    k = 3

    arr = [None] * k

    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)

    head = mergeKLists(arr)

    printList(head)