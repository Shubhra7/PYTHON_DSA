
# Given two strings, write a method to decide if one 
# is a permutation of the other.

# https://youtu.be/e7AxCPzcBtg?t=656

# def valid_copy(s1,s2):
#     f1=[0]*26
#     f2=[0]*26
#     for i in s1:
#         f1[ord(i)-ord('A')]+=1
#     for i in s2:
#         f2[ord(i)-ord('A')]+=1
#     for i in range(26):
#         if f1[i]!=f2[i]:
#             return False
#     return True

from collections import Counter
def valid_copy(s1,s2):
    return Counter(s1)==Counter(s2)

s1='HELLO'
s2='EHLLO'
print(valid_copy(s1,s2))