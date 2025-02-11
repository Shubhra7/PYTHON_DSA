# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# https://www.youtube.com/watch?v=aZNaLrVebKQ
"""
Input: preorder = [3,9,20,15,7],
inorder = [9,3,15,20,7]

Output: [3,9,20,null,null,15,7]
"""
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildT(preorder,preStart,preEnd,inorder,inStart,inEnd,inMap):
    if(preStart>preEnd or inStart>inEnd):
        return None
    root = TreeNode(preorder[preStart])
    inRoot = inMap[root.val]
    numLeft = inRoot-inStart

    root.left=buildT(preorder,preStart+1,preStart+numLeft, inorder,inStart,inRoot-1,inMap)
    root.right=buildT(preorder,preStart+numLeft+1,preEnd, inorder,inRoot+1,inEnd,inMap)

    return root

def level_order_traversal(root):
    if root is None:
        print("N ",end="")
        return
    queue = deque([root])
    while queue:
        cur = queue.popleft()
        if cur is None:
            print("N ",end="")
            continue
        print(cur.val,end=" ")
        queue.append(cur.left)
        queue.append(cur.right)

def buildTree(preorder,inorder):
    inMap={}
    for i in range(len(inorder)):
        inMap[inorder[i]]=i
    root = buildT(preorder,0,len(preorder)-1, inorder,0,len(inorder)-1,inMap)
    return root

preorder = [3,9,20,15,7]
inorder= [9,3,15,20,7]

root = buildTree(preorder,inorder)
level_order_traversal(root)

