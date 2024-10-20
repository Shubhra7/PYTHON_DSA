maxi = 0
maxi2=0
arr = [5,4,2,1,2,1,63]

# for i in arr:
#     if(maxi < i):
#         maxi2 = maxi
#         maxi = i
#     elif(maxi2 < i):
#         maxi2 = i
# print(maxi2)

ans = sorted(list(set(arr)), reverse=True)
print(ans[1])
