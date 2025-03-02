# https://www.youtube.com/watch?v=zMdbdGJNlh4

"""
Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
"""

class Solution:
	def prevSmaller(self, A):
            res=[-1]*len(A)
            stack=[]
            for i in range(len(A)):
                while stack and stack[-1]>=A[i]:
                    stack.pop()
                if stack:
                    res[i]=stack[-1]
                else:
                    res[i]=-1
                stack.append(A[i])
            return res

obj=Solution()
print(obj.prevSmaller([4, 5, 2, 10, 8]))