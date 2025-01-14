def find_sum(arr,tar):
    n=len(arr)
    ind=[0,n+1]
    for i in range(n):
        ans=0
        for j in range(i,n):
            ans += arr[j]
            print(ans)
            if ans==tar:
                print("Bro")
                if ind[1]-ind[0] >(j-i):
                    ind[0],ind[1]=i,j
        print("hello ",i,"  ",ind)
    return ind

arr=[1,2,3,7,5]
print(find_sum(arr,12))
# print(find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],15))