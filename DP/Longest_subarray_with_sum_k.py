# https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_5713505?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems&leftPanelTabValue=PROBLEM


# https://youtu.be/frf7qxiN2qU?si=N5XEaBebt2oX9FjQ

"""
Problem statement
Ninja and his friend are playing a game of subarrays. They have an array ‘NUMS’ of length ‘N’. 
Ninja’s friend gives him an arbitrary integer ‘K’ and asks him to find the length of the longest 
subarray in which the sum of elements is equal to ‘K’.
Ninjas asks for your help to win this game. Find the length of the longest subarray in which the 
sum of elements is equal to ‘K’.
If there is no subarray whose sum is ‘K’ then you should return 0.

Example:
Input: ‘N’ = 5,  ‘K’ = 4, ‘NUMS’ = [ 1, 2, 1, 0, 1 ]

Output: 4

There are two subarrays with sum = 4, [1, 2, 1] and [2, 1, 0, 1]. 
Hence the length of the longest subarray with sum = 4 is 4.
"""

def getLongestSubarray(nums, k):
    # Write your code here
    h={}  # for storing  prefixsum: index
    sum1=0
    maxi=0
    for i in range(len(nums)):
        sum1+=nums[i]
        if sum1==k:
            maxi=max(maxi,i+1)
            
        if h.get((sum1-k),-1)!=-1:  # *** -1 is very important because we store index, 0 will clash with index 0
            maxi=max(maxi,i-h[sum1-k])
            
        if h.get(sum1,-1)==-1:
            h[sum1]=i
    return maxi

print(getLongestSubarray([ 1, 2, 1, 0, 1 ],4))  #0/p ==> 4
