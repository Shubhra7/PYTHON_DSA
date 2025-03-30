arr=[[1,2],[2,1],[3,-1]]
arr.sort(key=lambda x:x[1])
print(arr)
del arr[1]
print(arr)