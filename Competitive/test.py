
def find(total,arr):
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
        if (sum >= total):
            return i+1
    return -1
        

r=int(input("Enter:"))
unit=int(input())
arr=list(map(int,input().split()))

total = r*unit

print(find(total,arr))