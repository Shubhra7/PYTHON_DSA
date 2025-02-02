from copy import deepcopy

# https://www.youtube.com/watch?v=f2ic2Rsc9pU
#----------------------------------
#      Appoarch= 2     Using Swap
#----------------------------------
def recurPermute_Appr_2(index,sarr,ans):
    if index==len(sarr):
        ans.append(deepcopy("".join(sarr)))
        return
    for i in range(index,len(sarr)):
        sarr[index],sarr[i] = sarr[i],sarr[index] # swao
        recurPermute_Appr_2(index+1,sarr,ans)
        sarr[index],sarr[i] = sarr[i],sarr[index] #for thik kore in previous version

#https://www.youtube.com/watch?v=YK78FU5Ffjw
#----------------------------------
#      Appoarch= 1     Using map
#----------------------------------

def recurPermute(sarr, ds, ans, freq):
    if len(ds) == len(sarr):
        ans.append(deepcopy("".join(ds)))
        return  # Added return statement

    for i in range(len(sarr)):
        if not freq[i]:  # Using Boolean check
            ds.append(sarr[i])
            freq[i] = True  # Mark as used
            recurPermute(sarr, ds, ans, freq)
            freq[i] = False  # Backtrack
            ds.pop()  # Corrected list removal

# s = "ABC"
s="kk"
sarr = list(s)
ans = []
ds = []
freq = [False] * len(sarr)  # Boolean list

recurPermute(sarr, ds, ans, freq)
# recurPermute_Appr_2(0,sarr,ans)
print(list(set(ans)))
