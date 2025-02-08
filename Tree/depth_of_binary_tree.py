#Driver Code Starts{
# Python program to find the height of a binary 
# tree using depth-first search (DFS) approach.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
#Driver Code Ends }


# Returns height which is the number of edges
# along the longest path from the root node down 
# to the farthest leaf node.
def height(root):
    if root is None:
        return -1

    # compute the height of left and right subtrees
    lHeight = height(root.left)
    rHeight = height(root.right)

    return max(lHeight, rHeight) + 1


#Driver Code Starts{
if __name__ == "__main__":
  
    # Representation of the input tree:
    #     12
    #    /  \
    #   8   18
    #  / \
    # 5   11
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)

    print(height(root))
#Driver Code Ends }