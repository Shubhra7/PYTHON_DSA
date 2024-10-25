def max_matc(m,n):
    count = 0
    bound = min(len(m),len(n))
    for i in range(1,bound+1):
        if(m[-i] == n[-i]):
            count += 1
        else:
            return count
    return count

def max_rhyme(arr,match):
    mini = 0
    ans=""
    for i in arr:
        val = max_matc(i,match)
        print(val,": ",i)
        if(val > mini or (val == mini and len(i)<len(ans))):
            mini=val
            ans = i
    return ans
        

arr = ["gender","blender","blunder","under"]
match = "thunder"

print(max_rhyme(arr,match))