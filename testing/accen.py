
def moveHy(s):
    ans=""
    count=0
    for i in s:
        if i=='-':
            count+=1
        else:
            ans+=i
    return ('-'*count + ans)
        

s="Move-Hyphens-to-Front"
p="String-Compare"
print(moveHy(s))
print(moveHy(p))