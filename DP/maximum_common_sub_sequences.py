# Link: https://youtu.be/NPZn9jBrX8U?si=fTiqRril12rzgJJU
# leecode: https://leetcode.com/problems/longest-common-subsequence/

def find_lcs(ind1,ind2,text1,text2):
        prev = [0 for i in range(ind2+1)]
        for i in range(1,ind1+1):
            cur=[0 for i in range(ind2+1)]
            for j in range(1,ind2+1):
                if(text1[i-1] == text2[j-1]):
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(prev[j], cur[j-1])  # Crucial for sub sequences
            prev=cur
        return prev[ind2]
def longestCommonSubsequence(text1: str, text2: str):
    n,m = len(text1),len(text2)
    return find_lcs(n,m,text1,text2)

word1,word2 = map(str,input().split())
print(longestCommonSubsequence(word1,word2))