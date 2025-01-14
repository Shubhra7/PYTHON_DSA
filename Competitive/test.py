def find_sum(arr,tar):
    n=len(arr)
    ind=[-1,-1]
    for i in range(n):
        ans=0
        for j in range(i,n):
            ans += arr[j]
            # print(ans)
            if ans==tar:
                return [i+1,j+1]
    if ind[0]==-1:
        return [-1]
    else:
        return ind

arr=[1,2,3,7,5]
print(find_sum(arr,12))
print(find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],15))
print(find_sum([5,3,4],2))