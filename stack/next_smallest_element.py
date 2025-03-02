def nse(a):
    res=[-1]*len(a)
    stack=[]
    n=len(a)
    for i in range(n-1,-1,-1):
        while stack and stack[-1]>a[i]:
            stack.pop()
        if stack:
            res[i]=stack[-1]
        else:
            res[i]=-1
        stack.append(a[i])
    return res
A = [4, 5, 2, 10, 8]
print(nse(A))