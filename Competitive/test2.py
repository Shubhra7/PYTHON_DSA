def match(a,b):
    i=len(a)-1
    j=len(b)-1
    count = 0
    while(i>=0 and j>=0):
        if(a[i]==b[j]):
            count += 1
        else:
            return count
        i -= 1
        j -= 1
    return count

def max_rhyme(arr,word):
    ans=""
    maxi=0
    for i in arr:
        val = match(i,word)
        print(i," : ",val)
        if(val > maxi):
            maxi = val
            ans = i
        elif(val == maxi):
            if(len(ans) > len(i)):
                ans=i
    return ans

arr = ['gender','blender','blunder','under']
word = 'thunder'

print(max_rhyme(arr,word))