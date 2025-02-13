import re
sen="Write a  program  ##  the long"
li=[word for word in re.split(r'\s+|#+',sen) if word]  #To avoid space and conjucate things
print(li)