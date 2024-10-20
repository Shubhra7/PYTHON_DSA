def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def permut(s):
    d={}
    vow = ['a','e','i','o','u']
    count = 0
    for i in range(len(s)):
        if s[i] not in vow:
            count += 1
            d[s[i]] = d.get(s[i],0)+1
    dual=1
    for i in d.values():
        if i > 1:
            dual *= fact(i)
    print(count)
    return int(fact(count)/dual)


s="ybghjahebuyitob"
print(permut(s.lower()))


