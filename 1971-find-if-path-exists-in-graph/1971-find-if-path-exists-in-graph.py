class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        visited=set()
        q=deque()
        q.append(source)
        while q:
            size=len(q)
            for _ in range(size):
                x=q.popleft()
                if x==destination:
                    return True
                visited.add(x)
                for nei in g[x]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        return False