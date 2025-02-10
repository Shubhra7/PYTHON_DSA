#Driver Code Starts{
# Python Program Invert a Binary Tree using Recursive Postorder

from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
#Driver Code Ends }


# Function to return the root of inverted tree
def mirror(root):
    if root is None:
        return None
    lefthand=mirror(root.left)
    righthand=mirror(root.right)
    root.left=righthand
    root.right=lefthand
    return root
    
# Print tree as level order
def levelOrder(root):
    if root is None:
        print("N ", end="")
        return

    queue = deque([root])

    while queue:
        curr = queue.popleft()

        if curr is None:
            print("N ", end="")
            continue

        print(curr.data, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)


#Driver Code Starts{
if __name__ == "__main__":
    # Input Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    mirror(root)

    # Mirror Tree:
    #       1
    #      / \
    #     3   2
    #        / \
    #       5   4
    levelOrder(root)


#Driver Code Ends }