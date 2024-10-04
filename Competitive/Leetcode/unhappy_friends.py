# Link: https://leetcode.com/problems/count-unhappy-friends/submissions/1411609573/

n=4
preferences = [[1,2,3], [3,2,0], [3,1,0], [1,2,0]]  
pairs = [[0,1], [2,3]]

# -----------------------------------
#### *******  METHOD-1************
# -----------------------------------

priority = {}
#making priority dictonary
# jar stha pair hoyacha tar aga karor preferences e kao ache kina

for p1, p2 in pairs:
    priority[p1] = preferences[p1][:preferences[p1].index(p2)]
    priority[p2] = preferences[p2][:preferences[p2].index(p1)]
print(priority)
#start the iteration
res = 0 #act as a counter for unhappy friends
for p1 in priority:
    for p2 in priority[p1]:    # Checking ami jake valobasi, seoo ki amkee valo base
        if p1 in priority[p2]:     # amr list e je aga acha tar list eo ki ami aga achi check!!
            # print(p1)
            res += 1
            break
print(res)
# return res

# -----------------------------------
### ******* METHOD - 2 **********
# -----------------------------------


# premap = [[99 for i in range(n)] for i in range(n)]

# for i in range(0,n):
#     for j in range(0,n-1):
#         premap[i][preferences[i][j]] = j

# for i in premap:
#     print(i)

# flag = [False for i in range(n)]

# for i in range(0,len(pairs)):
#     a= pairs[i][0]
#     b= pairs[i][1]
#     prefB = premap[a][b]
#     prefA = premap[b][a]
#     for j in range(i+1,len(pairs)):
#         ele1 = pairs[j][0]
#         ele2 = pairs[j][1]
#         prefEle2 = premap[ele1][ele2]
#         prefEle1 = premap[ele2][ele1]

#         if(prefB > premap[a][ele1] and prefEle2 > premap[ele1][a]):
#             flag[a]= True
#             flag[ele1]= True

#         if(prefB > premap[a][ele2] and prefEle1 > premap[ele2][a]):
#             flag[a]=True
#             flag[ele2] = True
        
#         if(prefA > premap[b][ele1] and prefEle2 > premap[ele1][b]):
#             flag[b]=True
#             flag[ele1] = True
        
#         if(prefA > premap[b][ele2] and prefEle1 > premap[ele2][b]):
#             flag[b]=True
#             flag[ele2]=True
        
#         unhappy = 0
#         for i in flag:
#             if(i):
#                 unhappy += 1
        
#         print(unhappy)
        
        

