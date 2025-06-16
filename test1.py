from collections import deque
def check(st):
    nd,sd = deque(),deque()
    for i in range(len(st)):
        if st[i].isdigit():
            nd.append(st[i])
        elif st[i]!=']':
            sd.append(st[i])
        else:
            ans=""
            ele=""
            allSt=""
            while ele!='[':
                allSt=ele+allSt
                ele=sd.pop()   
            cn=nd.pop()
            ans=allSt*int(cn)
            sd.append(ans)
    return sd

# st="3[a2[c]]"  #accaccacc
st="3[a]2[bc]"  #aaabcbc
print("".join(check(st)))



