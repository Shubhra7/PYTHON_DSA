import re
input1 = "abc   bcd cda"
input2 = "abc bad"

# ans = re.split(r'\s+',input1)
ans = re.sub('[^ab]','#',input2)
print(ans)
print(len(ans))