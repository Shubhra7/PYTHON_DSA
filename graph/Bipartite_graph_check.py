# https://leetcode.com/problems/is-graph-bipartite/submissions/1669738151/
# https://youtu.be/-vu34sct1g8?si=E6hmbvimtbfKtfKq

"""
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
"""
# linear without cycle graph is always is bipartite graph
# graph cycle with odd number node is not biparatite graph
# graph cycle with even number node is  biparatite graph
# if the total graph can be coloured by Two colour then it is bipartite graph 


from collections import deque
class Solution:
    def isBipartite(self, graph):
        ####################
        #       Used BFS
        ####################
        def check(node,graph,coloured):
            q=deque()
            coloured[node]=0
            q.append(node)
            while q:
                nd=q.popleft()
                for subN in graph[nd]:
                    # when the subnode is not coloured
                    if coloured[subN]==-1:
                        coloured[subN]= not(coloured[nd])
                        q.append(subN)
                    #if same coloured as parent
                    elif coloured[subN]==coloured[nd]:
                        return False
            return True

        V=len(graph)
        coloured=[-1]*V
        # DO bcz maybe seperate component present
        for i in range(V):
            if coloured[i]==-1:
                if( not check(i,graph,coloured)):
                    return False
        return True
    
obj=Solution()
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]  #False
graph = [[1,3],[0,2],[1,3],[0,2]]  #True
print("Using BFS: ",end="")
print(obj.isBipartite(graph))


class Solution:
    def isBipartite(self, graph):
        ####################
        #       Used DFS
        ####################
        def check(node,col,graph,colour):
            colour[node]=col
            for subN in graph[node]:
                if colour[subN]==-1:
                    if(not check(subN,not(col),graph,colour)):
                        return False
                elif colour[subN] == colour[node]:
                    return False
            return True
        V=len(graph)
        colour=[-1]*V
        for i in range(V):
            if colour[i]==-1:
                if not check(i,0,graph,colour):
                    return False
        return True
    
obj=Solution()
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]  #False
graph = [[1,3],[0,2],[1,3],[0,2]]  #True
print("Using DFS: ",end="")
print(obj.isBipartite(graph))


        