def find_sum(arr,sum):
    h={}
    currentSum=0
    for i in range(len(arr)):
        currentSum += arr[i]
        if currentSum == sum:
            return [0,i]
        if h.get(currentSum-sum,-1) != -1:
            return [h[currentSum-sum]+1,i]
        h[currentSum]=i
    return [-1,-1]

# print(find_sum([-4,-6,-1,1],-10))
print(find_sum([-1,0,-1,0],0))