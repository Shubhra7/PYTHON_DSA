# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/article/MzI5Mzc2
# https://leetcode.com/problems/path-sum-iii/description/

#Driver Code Starts{
# Python Program to Count all K Sum Paths in Binary Tree
# Using Prefix sum Technique
from collections import defaultdict

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
#Driver Code Ends }


# Function to find paths in the tree which have their sum equal to K
def countPathsUtil(node,cur_sum,target,answer,d):
    if node is None:
        return
    cur_sum += node.data
    if cur_sum-target in d:
        answer[0] += d[cur_sum-target]
    d[cur_sum]+=1
    if node.left:
        countPathsUtil(node.left,cur_sum,target,answer,d)
    if node.right:
        countPathsUtil(node.right,cur_sum,target,answer,d)
    d[cur_sum]-=1
    

# Function to find the paths in the tree which have their sum equal to K
def countAllPaths(root, k):
    prefSums = defaultdict(int)
    prefSums[0]=1
    answer=[0]
    countPathsUtil(root,0,k,answer,prefSums)
    return answer[0]


#Driver Code Starts{
if __name__ == "__main__":
    # Create a sample tree:
    #        8
    #      /  \
    #     4    5
    #    / \    \
    #   3   2    2
    #  / \   \
    # 3  -2   1

    root = Node(8)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.right = Node(2)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right.right = Node(1)

    k = 7
    print(countAllPaths(root, k))

#Driver Code Ends }