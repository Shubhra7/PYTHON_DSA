# https://leetcode.com/problems/flood-fill/
# https://youtu.be/C-2_uSRli8o?si=AMMauqvTAsQ1hTKp

"""
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

"""

############################################
#       DONE by DFS
############################################


class Solution:
    def floodFill(self, image, sr, sc, color):
        def dfs(image,sr,sc,color,iniColor):
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            image[sr][sc]=color
            row,col=len(image),len(image[0])
            for m,n in directions:
                newR,newC = sr+m,sc+n
                if(newR in range(row) and newC in range(col) and image[newR][newC]==iniColor):
                    dfs(image,newR,newC,color,iniColor)
        iniColor=image[sr][sc]
        if iniColor==color:  #very important check otherwise it will go infinity loop
            return image
        dfs(image,sr,sc,color,iniColor)
        return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
obj=Solution()
print(obj.floodFill(image,sr,sc,color))  #Output: [[2,2,2],[2,2,0],[2,0,1]]


        