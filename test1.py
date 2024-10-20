def max_rhyme(arr,given):
    mini = min([len(i) for i in arr])
    ans=0
    val=""
    maxi=0
    for j in arr:
        ans=0
        for i in range(1,mini+1):
            if(j[-i] != given[-i]):
                break
            ans += 1
        if(maxi < ans):
            val = j
            maxi=ans
        if(maxi == ans):
            if(len(val) > len(j)):
                val=j
    print(maxi)
    print(val)
        

arr=["gender","blender","blunder","under"]
given = "thunder"

max_rhyme(arr,given)