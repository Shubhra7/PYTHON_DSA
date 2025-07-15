# https://youtu.be/_BvEJ3VIDWw?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
"""
Input:
arr[] = {2, 5, 7}
start = 3, end = 30
Output:
2
Explanation:
Step 1: 3*2 = 6 % 100000 = 6 
Step 2: 6*5 = 30 % 100000 = 30
"""

from typing import List
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        mod=100000
        q=deque()
        dist=[float('inf')]*100000
        
        if start==end:
            return 0
        
        q.append((0,start))
        while q:
            steps,mul = q.popleft()
            for it in arr:
                newMul = (mul*it) % mod
                if newMul == end:
                    return steps+1
                if steps+1 < dist[newMul]:
                    dist[newMul]=steps+1
                    q.append((steps+1,newMul))
        return -1
        
arr= [2, 5, 7]
start = 3
end = 30
obj=Solution()
print(obj.minimumMultiplications(arr,start,end))  #2