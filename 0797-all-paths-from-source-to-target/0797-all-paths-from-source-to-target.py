class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        n=len(graph)
        def dfs(node,temp):
            temp.append(node)
            if node==n-1:
                res.append(temp[:])
                return
            
            for nei in graph[node]:
                dfs(nei,temp)
                temp.pop()
        dfs(0,[])
        return res