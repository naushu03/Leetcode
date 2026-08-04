class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        cnt=0
        while q:
            node=q.popleft()
            cnt+=1
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        return cnt==numCourses