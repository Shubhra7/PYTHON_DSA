from collections import Counter
def delete_earn(nums):
    d=Counter(nums)
    mini = min(d)
    maxi = max(d)
    pick=mini*d[mini]
    nopick=0
    for i  in range(mini+1,maxi+1):
        newpick = nopick+ i*(d[i])
        nonewpick = max(pick,nopick)
        pick = newpick
        nopick = nonewpick
        
    return max(pick,nopick)


nums = [2,2,3,3,3,4]
print(delete_earn(nums))