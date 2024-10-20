from collections import Counter

def delete_earn(nums):
    d=Counter(nums)
    low=min(nums)
    high = max(nums)

    pick= low*d[low]
    nopick=0
    for i in range(low+1,high+1):
        newpick = nopick + (i*d[i])
        newnopick = max(nopick,pick)

        pick=newpick
        nopick=newnopick
    return max(pick,nopick)

nums = [2,2,3,3,3,4]
print(delete_earn(nums))