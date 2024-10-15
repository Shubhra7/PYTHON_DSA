def match_count(i,match):
    count = 0
    x=len(i)-1
    y=len(match)-1
    while(x>=0 and y>=0 and i[x]==match[y]):
        count += 1
        x -= 1
        y -= 1
    return count

def max_rhy(arr,match):
    print("hi")
    ans=""
    maxi=0
    for i in arr:
        req = match_count(i,match)
        print(req)
        if(maxi < req):
            ans = i
            maxi = req
        elif(maxi == req):
            if(len(ans)>len(i)):
                ans=i
    print("hi2")
    return ans


arr = ["gender","blender","blunder","under"]
match = "thunder"
print(max_rhy(arr,match))