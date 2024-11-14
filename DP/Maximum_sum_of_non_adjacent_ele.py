# Similar like delete and earn normal
# link: https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261?leftPanelTabValue=PROBLEM
# link: https://youtu.be/GrMBfJNk_NY?si=akFdyy_1AAxYAYEb

#------------------------------
#   Mine do (normal like delete and earn in leetcode Accenture folder)
#------------------------------

arr=[1,2,3,1,3,5,8,1,9]

pick=arr[0]
notpick=0

for i in range(1,len(arr)):
    newpick = notpick + arr[i]
    newnotpick = max(pick,notpick)

    pick,notpick = newpick,newnotpick

print(max(pick,notpick))

#------------------------------
#   Striver do
#------------------------------

arr=[1,2,3,1,3,5,8,1,9]

prev=arr[0]
prev2=0

for i in range(1,len(arr)):
    take = arr[i]
    if(i>1):
        take += prev2
    notake = 0 + prev
    
    curi = max(take,notake)
    prev2, prev = prev, curi

print(prev)