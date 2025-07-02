class Solution:
    def isAlienSorted(self, words, order):
        d = {ch: i for i, ch in enumerate(order)}
        n = len(words)
        for i in range(n - 1):
            st1 = words[i]
            st2 = words[i + 1]
            leng = min(len(st1), len(st2))
            for j in range(leng):
                if st1[j] != st2[j]:
                    if d[st1[j]] > d[st2[j]]:
                        return False
                    break  # Found differing char, stop comparing further
            else:
                # If all characters so far are same, longer word should not come before shorter one
                if len(st1) > len(st2):
                    return False
        return True
        
        
obj=Solution()
words = ["word","world","row"]
# words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(obj.isAlienSorted(words,order))
