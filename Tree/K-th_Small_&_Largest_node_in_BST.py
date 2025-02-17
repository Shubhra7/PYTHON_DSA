# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/find-k-th-smallest-element-in-bst                                
# **** Above is valid when k elements are not present !!!****                     

# https://www.youtube.com/watch?v=9TJYWh0adfk

# Definition of TreeNode class
# for a binary tree node
class TreeNode:
    def __init__(self, x):
        # Value of the node
        self.val = x
        
        # Pointer to the left child node
        self.left = None
        
        # Pointer to the right child node
        self.right = None

# Solution class to find Kth smallest and largest elements
class Solution:
    def __init__(self):
        pass

    # Helper function to perform reverse inorder
    # traversal to find Kth largest element
    def reverse_inorder(self, node, counter, k, k_largest):
        if not node or counter[0] >= k:
            return
        
        # Traverse right subtree
        self.reverse_inorder(node.right, counter, k, k_largest)

        # Increment counter after
        # visiting right subtree
        counter[0] += 1

        # Check if current node
        # is the Kth largest
        if counter[0] == k:
            k_largest[0] = node.val
            return

        # Traverse left subtree if
        # Kth largest is not found yet
        self.reverse_inorder(node.left, counter, k, k_largest)

    # Helper function to perform inorder
    # traversal to find Kth smallest element
    def inorder(self, node, counter, k, k_smallest):
        if not node or counter[0] >= k:
            return

        # Traverse left subtree
        self.inorder(node.left, counter, k, k_smallest)

        # Increment counter after visiting left subtree
        counter[0] += 1

        # Check if current node is the Kth smallest
        if counter[0] == k:
            k_smallest[0] = node.val
            return

        # Traverse right subtree if
        # Kth smallest is not found yet
        self.inorder(node.right, counter, k, k_smallest)

    def find_kth(self, root, k):
        k_smallest = [float('inf')]
        k_largest = [float('-inf')]
        # Counter to track visited nodes
        counter = [0]

        # Find Kth smallest element
        # (perform inorder traversal)
        self.inorder(root, counter, k, k_smallest)
        
        # Reset counter for Kth largest element
        counter[0] = 0
        # Find Kth largest element
        # (perform reverse inorder traversal)
        self.reverse_inorder(root, counter, k, k_largest)

        return k_smallest[0], k_largest[0]


# Function to perform an in-order traversal
# of a binary tree and print its nodes
def print_in_order(root):
    # Check if the current node
    # is null (base case for recursion)
    if not root:
        # If null, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    print_in_order(root.left)

    # Print the value of the current node
    print(root.val, end=" ")

    # Recursively call printInOrder
    # for the right subtree
    print_in_order(root.right)

# Creating a BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print("Binary Search Tree:")
print_in_order(root)
print()

solution = Solution()

# Find the Kth smallest and largest elements
k = 3
print("k:", k)
kth_elements = solution.find_kth(root, k)

print("Kth smallest element:", kth_elements[0])
print("Kth largest element:", kth_elements[1])
                                
                            