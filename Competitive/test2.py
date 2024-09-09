def rev(arr):
    return arr[::-1]

arr = [1,2,3,4,5]

# Method: 1
s=[0 for i in range(len(arr))]
k=2
n=len(arr)

for i in range(len(arr)):
    s[(i+k)%n]=arr[i]

print(s)

# Method: 2
# First reverse all
# reverse first k elements
# reverse lask n-k elements
k=2
arr=arr[::-1]
s1=rev(arr[:k])+(rev(arr[k:]))
print(s1)