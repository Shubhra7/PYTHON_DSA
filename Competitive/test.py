def mergeOverlap(arr):
		#Code here
    if len(arr)==0:
        return arr
    for i in range(len(arr)):
        left,right = arr[i][0],arr[i][1]
        b=[]
        for j in range(len(arr)):
            if i==j:
                continue
            else:
                lf,rg = arr[j][0],arr[j][1]
                if lf>=left and rg<=right:
                    continue
                b.append(arr[j])
        # arr=b
        print(b)
    return arr
print(mergeOverlap([[1,3],[2,4],[6,8],[9,10]]))
