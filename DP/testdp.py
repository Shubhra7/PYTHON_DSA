# import sys
# data=sys.stdin.read().split()
# print(data)
# arr=list(map(int,data))
# print(arr)

# import re
# arr="Ramu96 jau Kalu#**"
# arr=re.sub(r"[^A-Za-z0-9]","",arr)
# print(arr)

import re
arr = "Ramur*96 jau KaluR#**"
arr = re.sub(r"[Rr][^A-Za-z0-9]+", "", arr)
print(arr)
arr=re.sub("\s+","",arr)
print(arr)



arr=[1,2,3,4]
p=[2,4]
arr.extend(p)
# print(arr)