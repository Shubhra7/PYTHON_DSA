
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isLeaf(root):
    return not root.left and not root.right
def addLeftBoundary(root,res):
    cur=root.left
    while cur:
        if not isLeaf(cur):
            res.append(cur.data)
        if cur.left:
            cur=cur.left
        else:
            cur=cur.left
def addLeaves(root,res):
    if isLeaf(root):
        res.append(root.data)
        return
    if root.left:
        addLeaves(root.left,res)
    if root.right:
        addLeaves(root.right,res)
def addRightBoundary(root,res):
    cur=root.right
    temp=[]
    while cur:
        if not isLeaf(cur):
            temp.append(cur.data)
        if cur.right:
            cur=cur.right
        else:
            cur=cur.left
    for i in range(len(temp)-1,-1,-1):
        res.append(temp[i])

def BorderTraverse(root):
    res=[]
    if root is None:
        return res
    if not isLeaf(root):
        res.append(root.data)
    addLeftBoundary(root,res)
    addLeaves(root,res)
    addRightBoundary(root,res)
    return res



if __name__ == "__main__":
  
    # Representation of input binary tree:
    #           1
    #          /  \
    #         2     3
    #        / \   / \ 
    #       4   5 6   7
    #          / \
    #         8   9
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.left.right.left=Node(8)
    root.left.right.right=Node(9)


    res = BorderTraverse(root)
    
    for data in res:
        print(data, end=" ")

#Driver Code Ends }