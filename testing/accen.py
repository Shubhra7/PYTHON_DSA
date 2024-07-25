def findC(arr,num,diff):
    ans=0
    for i in arr:
        if(abs(i-num) <= diff):
            ans+=1
    if(ans>0):
        return ans
    else:
        return -1

arr=list(map(int,input().split()))
num=13
diff=2

print(findC(arr,num,diff))