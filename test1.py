def score(arr):
    hcount=0
    sc=0
    for i in arr:
        if(i=='H'):
            sc += 2
            hcount+=1
        else:
            sc -= 1
            hcount=0
        if(hcount==3):
            return sc
    return sc


arr1 = ['T','T','T']
print(score(arr1))