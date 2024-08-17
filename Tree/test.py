

def median(mat,right,left):
    while (right <= left):
        mid = left + (right - left)//2
        






matrix = [     [ 1, 5, 7, 9, 11 ],
      [ 2, 3, 4, 8, 9 ],
      [ 4, 11, 14, 19, 20 ],
      [ 6, 10, 22, 99, 100 ],
      [ 7, 15, 17, 24, 28 ]   ]


print(median(matrix,len(matrix),len(matrix[0])))