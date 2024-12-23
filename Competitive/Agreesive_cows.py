# https://www.naukri.com/code360/problems/aggressive-cows_1082559
# https://youtu.be/R_Mfw4ew-Vo?si=wNI5pfq8JtJcWKaR

"""
You are given an array with unique elements of stalls[], 
which denote the position of a stall. You are also given an 
integer k which denotes the number of aggressive cows. Your task 
is to assign stalls to k cows such that the minimum distance 
between any two of them is the maximum possible.

Examples :

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3

Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
"""

def possible_place_cow(stalls,mid,k):
    count_cow = 1
    last = stalls[0]
    for i in range(1,len(stalls)):
        val = stalls[i]-last
        if val>=mid:
            count_cow += 1
            last = stalls[i]
        if count_cow >= k:
            return True
    return False


def aggressiveCows(stalls, k):
    # Write your code here.
    low = 1
    stalls.sort()
    high = stalls[-1]-stalls[0]
    while low<= high:
        mid = low + (high-low)//2
        if(possible_place_cow(stalls,mid,k)):
            low = mid+1
        else:
            high=mid-1
    return high

print(aggressiveCows([1, 2, 4, 8, 9],3))   #3