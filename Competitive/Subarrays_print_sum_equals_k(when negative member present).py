# https://www.naukri.com/code360/problems/subarray-with-given-sum_842487?leftPanelTabValue=PROBLEM

def subarraySum(arr, sum):
    # Write your function here.
    h={}
    currentSum=0
    for i in range(len(arr)):
        currentSum += arr[i]
        if currentSum == sum:
            return [0,i]
        print(currentSum)
        print(sum-currentSum)
        print(h)
        print("----------------------")
        if h.get(currentSum-sum,-1) != -1:
            return [h[currentSum-sum]+1,i]
        h[currentSum]=i
    # print(h)
    return [-1,-1]

print(subarraySum([-3 ,-9 ,10,-29,10,0],-19))  #o/p==> [2,3]