arr = [5,4,2,1,2,1,3]
s=set(arr)
l=sorted(s,reverse=True)
if(len(l) > 1):
    print(l[1])
else:
    print("Not possible")
