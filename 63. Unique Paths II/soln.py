class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==0:
            obstacleGrid[0][0]=-1 # stand for 1 possibility
        else: # obstacleGrid[0][0]==-1
            return 0 # cant go furthere
        for i,r in enumerate(obstacleGrid):
            for j,x in enumerate(r):
                if x==1: # is an obstacle, set to 0
                    obstacleGrid[i][j]=0
                else: # not an obstacle, count paths
                    if i>0: # ensure in-range
                        obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                    if j>0: # ensure in-range
                        obstacleGrid[i][j]+=obstacleGrid[i][j-1]
        return -obstacleGrid[-1][-1] # eliminate the minus sign
                    
