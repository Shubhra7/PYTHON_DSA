
def Score(arr):
    count = 0
    Score = 0
    for i in range(len(arr)):
       if (arr[i] == 'H'):
            Score += 2
            count += 1
       else:
           count=0
           Score -= 1
       if(count == 3):
           return Score
    return Score
           
arr = ['H','T','H','H','T','T','H','T','H','H','T']
arr1 = ['H','T','H','H','T','T','H','T','H','H','H','T']

print(Score(arr))
print(Score(arr1))