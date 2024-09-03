import re
input1 = "abc bcd cda"
input2 = "abc bad"

# ans = re.split(r'\s+',input1)
ans1, ans2 = 0,0
for i in input1:
    if(i==' '):
        ans1 += 1
for i in input2:
    if(i==' '):
        ans2 += 1
    
if (abs(ans2 - ans1) % 2==0):
    print('Even:',abs(ans1-ans2))
else:
    print('Odd:',abs(ans1-ans2))