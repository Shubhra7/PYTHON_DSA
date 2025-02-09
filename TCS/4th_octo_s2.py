# https://leetcode.com/problems/jump-game/description/

# You are given an integer arry nums. You are initially positioned at the array's first
# index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise. 

# i/p = [2,3,1,1,4]
# o/p = True

# i/p = [3,2,1,0,4]
# o/p = False

def check(arr):
    maxi=0   # maxi means Highest koto index obdhi jeta parchi
    for i in range(len(arr)):
        if i>maxi:
            return False
        maxi = max(maxi, i+arr[i])
    return True

arr = list(map(int,input().split(',')))
print("Answer is: ",check(arr))