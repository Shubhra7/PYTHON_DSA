import sys

arr = [5,4,2,1,2,1,3]
mini, mini2 = arr[0],arr[0]

for i in range(len(arr)):
    if mini > arr[i]:
        mini2 = mini
        mini = arr[i]
    elif(mini2 > arr[i] and mini != arr[i]):
        mini2 = arr[i]

print(mini2)