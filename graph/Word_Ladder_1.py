# https://www.geeksforgeeks.org/problems/word-ladder/1
# https://youtu.be/tRPda0rcf8E?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
"""
Input:
wordList = {"des","der","dfr","dgt","dfs"}
startWord = "der", targetWord= "dfs",
Output:
3
Explanation:
The length of the smallest transformation
sequence from "der" to "dfs" is 3
i,e "der" -> "dfr" -> "dfs".
"""


# Use BFS and 
# Check from a to z change and check for every index

from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        # Code here
        q = deque()
        q.append([startWord, 1])
        wordsSt = set(wordList)

        if startWord in wordsSt: # if startWord present then remove
            wordsSt.remove(startWord)

        while q:
            ele = q.popleft()
            word = ele[0]
            steps = ele[1]

            if word == targetWord:
                return steps

            for i in range(len(word)):
                for ch in range(26): # checking word from a to z for new word 
                    newWord = word[:i] + chr(ord('a') + ch) + word[i+1:]
                    if newWord in wordsSt:
                        wordsSt.remove(newWord)
                        q.append([newWord, steps + 1])

        return 0


obj=Solution()
wordList = {"des","der","dfr","dgt","dfs"}
startWord = "der"
targetWord= "dfs"
print("The Shortest path distance: ",end=" ")
print(obj.wordLadderLength(startWord,targetWord,wordList))  #3

		