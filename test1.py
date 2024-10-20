# arr=[2,3,-8,7,-1,2,3]
# arr=[-2,-4]
arr=[5,4,1,7,8]

# arr=[5,4,-1,7,8]
sum=arr[0]
ans=arr[0]
for i in range(1,len(arr)):
    sum = max(arr[i],sum + arr[i])
    ans = max(ans,sum)

print(ans)
