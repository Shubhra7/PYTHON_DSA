# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/


# We use LPS because it would be like mirror image
# so if the last matches element from the second side we got then after that we can check
# Like mota vai video [match ........... match ............ match]

"""
txt = "aabaacaadaabaaba"
pat = "aaba"

o/p == > 0 9 12 
"""

def construct_LPS(pat,lps):
    j=0
    i=1
    n=len(pat)

    while i<n:
        if(pat[i] == pat[j]):
            j += 1
            lps[i] = j
            i += 1
        else:
            if j!=0:
                j = lps[j-1]
            else:
                lps[i]=0
                i += 1

def search(pat,txt):
    n=len(txt)
    m=len(pat)

    lps = [0]*m
    res=[]

    construct_LPS(pat,lps)
    print(lps)

    # Again same like lps to check pattern
    i,j = 0,0

    while i < n:
        if(txt[i] == pat[j]):
            i += 1
            j += 1
            # check total pattern done or not??
            if j==m:
                res.append(i-j)
                #to avoid the unneccesary check like MIRROR IMAGE 
                j = lps[j-1]
        else:
            if j!=0:
                j = lps[j-1]
            else:
                i += 1
    return res


# txt = "aabaacaadaabaaba"
# pat = "aaba"   # o/p ==> 0 9 12
txt="geeksforgeeks"
pat="geek"
res = search(pat,txt)
print(res)