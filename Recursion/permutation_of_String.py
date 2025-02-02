from copy import deepcopy

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

s = "ABC"
sarr = list(s)
ans = []
ds = []
freq = [False] * len(sarr)  # Boolean list

recurPermute(sarr, ds, ans, freq)
print(ans)
