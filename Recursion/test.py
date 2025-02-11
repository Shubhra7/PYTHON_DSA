#Driver Code Starts{
# Python program to construct tree using 
# inorder and preorder traversals

from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Print tree as level order
def printLevelOrder(root):
    if root is None:
        print("N ", end="")
        return

    queue = deque([root])
    non_null = 1

    while queue and non_null > 0:
        curr = queue.popleft()

        if curr is None:
            print("N ", end="")
            continue
        non_null -= 1

        print(curr.data, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)
        if curr.left:
            non_null += 1
        if curr.right:
            non_null += 1
#Driver Code Ends }


# Function to find the index of an element in the array
def search(inorder, value, left, right):
    for i in range(left, right + 1):
        if inorder[i] == value:
            return i
    return -1

# Recursive function to build the binary tree.
def buildTreeRecur(inorder, preorder, preIndex, left, right):
    # For empty inorder array, return null
    if left > right:
        return None

    rootVal = preorder[preIndex[0]]
    preIndex[0] += 1

    # create the root Node
    root = Node(rootVal)

    # find the index of Root element in the in-order array.
    index = search(inorder, rootVal, left, right)

    # Recursively create the left and right subtree.
    root.left = buildTreeRecur(inorder, preorder, preIndex, left, index - 1)
    root.right = buildTreeRecur(inorder, preorder, preIndex, index + 1, right)

    return root

# Function to construct tree from its inorder and preorder traversals
def buildTree(inorder, preorder):
    preIndex = [0]
    return buildTreeRecur(inorder, preorder, preIndex, 0, len(preorder) - 1)


#Driver Code Starts{
if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder= [9,3,15,20,7]
    root = buildTree(inorder, preorder)
    printLevelOrder(root)

#Driver Code Ends }