from collections import defaultdict
def longestUniqueSubstr(s):
        # code here
        maxi=0
        h=defaultdict(int)
        i=1
        j=1
        while j<=len(s):
                # print(h)
                if h.get(s[j-1],0)!=0:
                        if h[s[j-1]]>=i:
                            maxi=max(maxi,j-i-1)
                            # print("Maxi:--- ",maxi)
                            i=h[s[j-1]]
                            h[s[j-1]]=j
                        else:
                              h[s[j-1]]=j
                else:
                    h[s[j-1]]=j
                j+=1
        maxi = max(maxi,j-i-1)
        return maxi

# print(longestUniqueSubstr("geeksforgeeks"))
# print(longestUniqueSubstr("abcdefabcbb"))
print(longestUniqueSubstr("fqvjgwdhmrgqkamm"))