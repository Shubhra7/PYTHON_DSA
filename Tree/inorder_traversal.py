#Driver Code Starts{
# Python code to print Inorder Traversal
# of Binary Tree using Morris Traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#Driver Code Ends }

def traverse(root,arr):
    if root is None:
        return
    traverse(root.left,arr)
    arr.append(root.data)
    traverse(root.right,arr)

def inOrder(root):
    arr=[]
    traverse(root,arr)
    return arr


#Driver Code Starts{

if __name__ == "__main__":
  
    # Representation of input binary tree:
    #           1
    #          / \
    #         2   3
    #        / \  
    #       4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    res = inOrder(root)
    
    for data in res:
        print(data, end=" ")

#Driver Code Ends }