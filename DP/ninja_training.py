# link: https://www.naukri.com/code360/problems/ninja-s-training_3621003?leftPanelTabValue=PROBLEM
# video: https://youtu.be/AE39gJYuRog?si=1BqYj6qDOuKaX6R5

# making the work with index 0 to 3 (3 for not any done)

'''Problem statement
Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?
You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
Detailed explanation ( Input/output format, Notes, Images )

Sample Input 1:
2
3
1 2 5 
3 1 1
3 3 3
3
10 40 70
20 50 80
30 60 90
Sample Output 1:
11
210
Explanation of sample input 1:
For the first test case,
One of the answers can be:
On the first day, Ninja will learn new moves and earn 5 merit points. 
On the second day, Ninja will do running and earn 3 merit points. 
On the third day, Ninja will do fighting and earn 3 merit points. 
The total merit point is 11 which is the maximum. 
Hence, the answer is 11.

'''
import copy

point=[[1,2,5],
     [3,1,1],
     [3,3,3]]
n=3

# point = [[10,40,70],
#          [20,50,80],
#          [30,60,90]]
# n=3

# ------------------------------
#---- Tabulation method-----(bottom up)
# ------------------------------

dp=[[-1 for i in range(5)]for j in range(n+1)]
# for storing the value je days*(konta krani aga)

dp[0][1]=max(point[0][0],point[0][2])
dp[0][0]=max(point[0][1],point[0][2])
dp[0][2]=max(point[0][1],point[0][0])
dp[0][3]=max(point[0][1],point[0][0],point[0][2])

for day in range(1,n):
    for last in range(4):
        dp[day][last]=0
        for task in range(3):
            if(task != last):
                value = point[day][task] + dp[day-1][task]
                # dp[day-1][task] ==> means o nija je task ta krini tar respect e val
                dp[day][last] = max(dp[day][last],value)
        
print(dp[n-1][3])


# ------------------------------
#---- Recursion method-----(Top down)
# ------------------------------

def find_max(day,point,dp,last):
    if(day == 0):
        maxi=0
        for i in range(len(point[0])):
            if(i != last):
                maxi = max(maxi,point[0][i])
        return maxi
    maxi=0
    for task in range(3):
        if(task != last):
            value = point[day][task] + find_max(day-1,point,dp,task)
            maxi = max(maxi,value)
        dp[day][task]=maxi
    return maxi


dps=[[-1 for i in range(5)]for j in range(n+1)]
ans = find_max(n-1,point,dps,3)
print(ans)


# ------------------------------
#-------- Most optimum ---------
# ------------------------------

prev = [0 for i in range(5)]

prev[1]=max(point[0][0],point[0][2])
prev[0]=max(point[0][1],point[0][2])
prev[2]=max(point[0][1],point[0][0])
prev[3]=max(point[0][1],point[0][0],point[0][2])

for day in range(1,n):
    temp = [0 for i in range(4)]
    for last in range(4):
        temp[last]=0
        
        for task in range(3):
            if(task != last):
                temp[last] = max(temp[last], point[day][task]+prev[task])

    prev = copy.deepcopy(temp)

print(prev[3])
