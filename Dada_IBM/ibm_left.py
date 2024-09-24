# Link: https://youtu.be/r3ayM0RCeZA?list=PLIUso1jSUd-Y9E2mxrhz5dqaldmZCtVxT&t=342

# arr=[2,4,3]
arr=[2,1,3]
ans=[0]

for i in range(1,len(arr)):
    coun = 0
    h=i-1
    while(h>=0):
        coun += (arr[i]-arr[h])

        h -= 1
    ans.append(coun)

print(ans)