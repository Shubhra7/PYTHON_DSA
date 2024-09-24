pwd = '100110'

l = list(pwd)

i,h=0,1
count = 0

while h<len(pwd):
    if(l[i]!=l[h]):
        temp=l[i]
        l[i]=l[h]
        l[h]=temp
        count += 1
        i +=1
    h+=1
print(count)
print(l)
    
