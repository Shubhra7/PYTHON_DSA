"""
Given an array ‘A’ consisting of ‘N’ integers and an integer ‘B’, 
find the number of subarrays of array ‘A’ whose bitwise XOR( ⊕ ) 
of all elements is equal to ‘B’.
"""

# Sample Input 1:
# 4 2
# 1 2 3 2
# Sample Output 1 :
# 3
# Explanation Of Sample Input 1:
# Input: ‘N’ = 4 ‘B’ = 2
# ‘A’ = [1, 2, 3, 2]
# Explanation: Subarrays have bitwise xor equal to ‘2’ are: [1, 2, 3, 2], [2], [2].

def subarraysWithSumK(a,b):
    # Write your code here
    xr=0
    k=b
    h={0:1}
    cnt=0
    for i in range(len(a)):
        xr ^= a[i]
        x = xr^k
        cnt += h.get(x,0)
        h[xr] = h.get(xr,0)+1
    return cnt
print(subarraysWithSumK([1,2,3,2],2))

