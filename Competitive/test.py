def findCount(arr,num,diff):
    count=0
    for i in range(len(arr)):
        if (abs(arr[i] - num) <= diff):
            print(arr[i])
            count+=1
    if (count > 0):
        return count
    else:
        return -1


arr=list(map(int,input().split()))
num=13
diff=2

print(findCount(arr,num,diff))