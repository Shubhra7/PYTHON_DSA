def pasRec(s):
    m=s[::-1]
    i=0
    j=2
    n=len(s)
    ans=""
    while (j <= n and i<=j ):
        val = int(m[i:j])
        if (val >= 65 and val <=90):
            ans = ans + chr(val)
            i=j
            j=j+2
        elif (val >= 97 and val <= 122):
            ans = ans + chr(val)
            i=j
            j=j+2
        else:
            j=j+1
    return ans


s=input()
print(pasRec(s))