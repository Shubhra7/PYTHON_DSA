# https://www.geeksforgeeks.org/problems/word-ladder-ii/1
# https://youtu.be/DREutrv2XD0?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

# after level complete then remove 

from collections import deque

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        st = set(wordList)
        q = deque()
        q.append([startWord])
        usedOnLevel = set()
        level = 0
        ans = []

        while q:
            vec = q.popleft()
            if len(vec) > level:
                level += 1
                for it in usedOnLevel:
                    st.remove(it)
                usedOnLevel.clear()

            word = vec[-1]
            if word == targetWord:
                if len(ans) == 0:
                    ans.append(vec)
                elif len(ans[0]) == len(vec):
                    ans.append(vec)

            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(ord('a') + j) + word[i+1:]
                    if newWord in st:
                        newPath = vec + [newWord]
                        q.append(newPath)
                        #marked as visited on Level
                        usedOnLevel.add(newWord)
        return ans

obj=Solution()
startWord = "der"
targetWord = "dfs"
wordList = {"des","der","dfr","dgt","dfs"}
print(obj.findSequences(startWord,targetWord,wordList))