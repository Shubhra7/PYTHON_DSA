from collections import Counter

def delete_earn(nums):
    d=Counter(nums)
    mini = min(nums)
    maxi = max(nums)
    pick = mini*d[mini]
    nopick = 0
    for i in range(mini+1,maxi+1):
        newpick = nopick + (i*d[i])
        newnopick = max(pick,nopick)

        pick,nopick = newpick, newnopick
    return max(pick,nopick)
nums = [2,2,3,3,3,4]
print(delete_earn(nums))