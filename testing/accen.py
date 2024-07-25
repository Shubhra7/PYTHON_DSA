r=int(input())
unit=int(input())
arr=list(map(int,input().split()))

if (len(arr)==0):
    print(-1)
else:
    total=r*unit
    for i in range(len(arr)):
        total-=arr[i]
        if total<=0:
            print(i+1)
            break
    else:
        print(0)