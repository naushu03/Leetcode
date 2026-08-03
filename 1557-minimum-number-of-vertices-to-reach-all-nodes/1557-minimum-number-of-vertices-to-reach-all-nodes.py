class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ind=[0]*n
        lst=[]
        for edge in edges:
            ind[edge[1]]+=1
            
        for i in range(n):
            if ind[i]==0:
                lst.append(i)
        return lst