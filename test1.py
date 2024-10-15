txt="snakewatergunwatergunsnake"
A=""
B=""
word=""
flag=1
for i in range(len(txt)):
    word += txt[i]
    if(word=='snake' or word=='water' or word=='gun'):
        if(flag==1):
            A+=word[0]
            flag=0
        else:
            B+=word[0]
            flag=1
        word=""
count = 0
for i in range(len(A)):
    if((A[i]=='s' and B[i]=='w')or(A[i]=='w' and B[i]=='g')or(A[i]=='g' and B[i]=='s')):
        count += 1
print(A)
print(B)
print("A wining times: ",count)
    

