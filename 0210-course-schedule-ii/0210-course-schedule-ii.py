class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x]+=1
        q=deque()
        order=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        if len(order)==numCourses:
            return order
        return []