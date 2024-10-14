def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

def permut(s):
    chk = ['a','e','i','o','u','A','E','I','O','U']
    d={}
    fac =0
    for i in s:
        if i not in chk:
            fac += 1
            d[i]=d.get(i,0)+1
    ans = 1
    if(len(d)==0):
        return 0
    for i in d.values():
        if(i>1):
            ans *= fact(i)
    
    return int(fact(fac)/ans)

s="ybghjahebuyitob"
print(permut(s))
