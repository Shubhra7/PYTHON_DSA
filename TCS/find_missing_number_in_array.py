# https://leetcode.com/problems/missing-number/description/
def missingNumber(arr):
    return sum(range(len(arr)+1))-sum(arr)
arr=[3,0,1]  #2
print(missingNumber(arr))