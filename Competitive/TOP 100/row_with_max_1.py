#Row With Maximum 1
# Link: https://prepinsta.com/python-program/find-row-with-maximum-no-of-1s/

matrix = [[0, 0, 0, 1],
          [0, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

max1 = 0
maxpos=0
for i in range(len(matrix)):
    total1 = matrix[i].count(1)
    if (total1 > max1):
        max1 = total1
        maxpos = i

print(maxpos+1)
