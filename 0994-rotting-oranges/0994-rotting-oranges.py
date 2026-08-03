class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        oneCount=0
        r,c=len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    oneCount+=1
        cnt=0
        while q and oneCount>0:
            size=len(q)
            cnt+=1
            for i in range(size):
                rows,cols=q.popleft()
                for dr,dc in (1,0),(-1,0),(0,1),(0,-1):
                    newR,newC=rows+dr,cols+dc
                    if newR>=0 and newR<r and newC>=0 and newC<c and grid[newR][newC]==1:
                        oneCount-=1
                        grid[newR][newC]=2
                        q.append((newR,newC))
        return cnt if oneCount==0 else -1
