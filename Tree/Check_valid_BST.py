# https://www.youtube.com/watch?v=f-sj7I5oXEI
# https://leetcode.com/problems/validate-binary-search-tree/description/

#Driver Code Starts{
# Python program to check if a tree is BST using Morris Traversal
import sys

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
#Driver Code Ends }

def check(root,minval,maxval):
    if root is None:
        return True
    if(minval>= root.data or maxval <=root.data):
        return False
    return check(root.left,minval,root.data) and check(root.right,root.data,maxval)
def isBST(root):
    return check(root,-sys.maxsize,sys.maxsize)

#Driver Code Starts{
if __name__ == "__main__":
  
    # Create a sample binary tree
    #     10
    #    /  \
    #   5    20
    #        / \
    #       9   25

    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.left = Node(9)
    root.right.right = Node(25)

    if isBST(root):
        print("True")
    else:
        print("False")

#Driver Code Ends }