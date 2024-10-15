st = "10111011"

arr = st.split('0')
print()
ans=""
for i in arr:
    val = chr(ord('A')-1+len(i))
    ans += val
print(ans)