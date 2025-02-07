from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
#Driver Code Ends }


def levelOrder(root):
    if root is None:
        return []

    # Create an empty queue for level order traversal
    q = deque()
    res = []

    # Enqueue Root
    q.append(root)
    currLevel = 0

    while q:
        len_q = len(q)
        res.append([])

        for _ in range(len_q):
            # Add front of queue and remove it from queue
            node = q.popleft()
            res[currLevel].append(node.data)

            # Enqueue left child
            if node.left is not None:
                q.append(node.left)

            # Enqueue right child
            if node.right is not None:
                q.append(node.right)
        currLevel += 1

    return res
      

#Driver Code Starts{
if __name__ == "__main__":
    # Create binary tree
    #      1         
    #     / \       
    #    3   2      
    #          \   
    #           4 
    #          /  \
    #         6    5
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.right.right = Node(4)
    root.right.right.left = Node(6)
    root.right.right.right = Node(5)

    # Perform level order traversal
    res = levelOrder(root)

    # Print the result
    for level in res:
        for data in level:
            print(data, end=" ")