class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows,cols=len(dungeon),len(dungeon[0])
        dp=[[0]*cols for i in range(rows)]
        dp[rows-1][cols-1]=1 if dungeon[rows-1][cols-1]>0 else 1-dungeon[rows-1][cols-1]
        for i in range(rows-2,-1,-1):
            dp[i][cols-1]=max(dp[i+1][cols-1]-dungeon[i][cols-1],1)
        for i in range(cols-2,-1,-1):
            dp[rows-1][i]=max(dp[rows-1][i+1]-dungeon[rows-1][i],1)
        for i in range(rows-2,-1,-1):
            for j in range(cols-2,-1,-1):
                x=min(dp[i][j+1],dp[i+1][j])
                y=x-dungeon[i][j]
                dp[i][j]=max(y,1)
        return dp[0][0]
