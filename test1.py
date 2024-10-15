def Score(arr):
    count=0
    score=0
    for i in arr:
        if(i=='H'):
            score += 2
            count += 1
        elif(i=='T'):
            score -= 1
            count = 0
        if(count == 3):
            return score
    return score

arr = ['H','T','H','H','T','T','H','T','H','H','T']
arr1 = ['H','T','H','H','T','T','H','T','H','H','H','T']
arr2 = ['H','H','H','T','T','T']
arr3 = ['T','T','T']

print(Score(arr))
print(Score(arr1))
print(Score(arr2))
print(Score(arr3))