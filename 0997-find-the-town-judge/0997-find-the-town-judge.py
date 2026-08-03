class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ind=[0]*(n+1)
        outd=[0]*(n+1)
        for x,y in trust:
            outd[x]+=1
            ind[y]+=1
        for i in range(1,n+1):
            if ind[i]==n-1 and outd[i]==0:
                return i
        return -1