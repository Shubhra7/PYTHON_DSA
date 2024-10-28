arr = [1,0,1,0,1]
goal = 2
positive=0
negative=1
sum=0
count=0

for i in range(len(arr)):
    sum += arr[i]
    if((sum-goal) == 0):
        count += negative
        positive += 1
    else:
        count += positive
        negative += 1
