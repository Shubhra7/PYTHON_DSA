#abc123xyz45 ==> 1 5 (vowel consonant)

st = input()
st=st.lower()
vowels='aeiou'
v=sum(1 for i in st if i in vowels)
c=sum(1 for i in st if i.isalpha() and i not in vowels)
print(v," ",c)