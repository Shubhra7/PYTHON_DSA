def Score(arr):
    hcount=0
    ans=0
    for i in range(len(arr)):
        if(arr[i] == 'H'):
            hcount += 1
            ans += 2
        if(arr[i] == 'T'):
            hcount = 0
            ans -= 1
        if(hcount == 3):
            return ans
    return ans



arr = ['H','T','H','H','T','T','H','T','H','H','T']
arr1 = ['H','T','H','H','T','T','H','T','H','H','H','T']
arr2 = ['H','H','H','T','T','T']
arr3 = ['T','T','T']

print(Score(arr))
print(Score(arr1))
print(Score(arr2))
print(Score(arr3))