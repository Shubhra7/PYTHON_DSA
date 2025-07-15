# https://youtu.be/rM3OIuLdHkI
"""
Input: target = 19, maxDoubles = 2
Output: 7
Explanation: Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19
"""

# Start from end because doing half of big number will take large steps


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        while target>1 and maxDoubles>0:
            ans+= 1 + (target%2)
            target //= 2
            maxDoubles -=1 
        return ans+target-1
        
obj=Solution()
target = 19
maxDoubles = 2
print(obj.minMoves(target,maxDoubles))