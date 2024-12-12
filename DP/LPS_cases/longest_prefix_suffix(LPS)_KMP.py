# Use Kmp method
# https://www.geeksforgeeks.org/longest-prefix-also-suffix/

# https://leetcode.com/problems/longest-happy-prefix/description/

"""
A string is called a happy prefix if is a non-empty prefix which is also a
suffix (excluding itself).
Given a string s, return the longest happy prefix of s. Return an empty 
string "" if no such prefix exists.

Example 1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), 
and suffix ("l", "el", "vel", "evel"). 
The largest prefix which is also suffix is given by "l".

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. 
They can overlap in the original string.
"""
def longest_prefix_suffix(s):
    n=len(s)
    lps = [0]*n
    i=1
    j=0
    while i<n:
        if(s[i] == s[j]):  #When matched
            j+=1
            lps[i]=j
            i+=1
        else:       # In Mismatches
            if j!=0:    # Case 1
                j=lps[j-1] 
            else:       # Case 2
                lps[i]=0
                i+=1
    print("The LPS of",s," is: ")
    print(list(s))
    print(lps)
    return s[:lps[n-1]]

# s = "ababab"        #o/p ==> abab
# s = "level"        #o/p ==> l
s = ")()())"        #o/p ==> l
print(longest_prefix_suffix(s))

