# https://youtu.be/Rezetez59Nk?si=O2Avo1X1pmzBzVUk

# # Given the root of a binary tree, return the length of the diameter of the tree.

# # The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# # The length of a path between two nodes is represented by the number of edges between them.
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Python program to find the diameter
# of a binary tree.

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Recursive function to find the height of root and 
# also calculate the diameter of the tree.
def diameterRecur(root, res):

    # Base case: tree is empty
    if root is None:
        return 0

    # find the height of left and right subtree
    # (it will also find of diameter for left 
    # and right subtree).
    lHeight = diameterRecur(root.left, res)
    rHeight = diameterRecur(root.right, res)

    # Check if diameter of root is greater
    # than res.
    res[0] = max(res[0], lHeight + rHeight)

    # return the height of current subtree.
    return 1 + max(lHeight, rHeight)

# Function to get diameter of a binary tree
def diameter(root):
    res = [0]
    diameterRecur(root, res)
    return res[0]

if __name__ == "__main__":

    # Constructed binary tree is
    #          5
    #        /   \
    #       8     6
    #      / \   /
    #     3   7 9
    root = Node(5)
    root.left = Node(8)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(9)

    print(diameter(root))
