class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        heap=[(0,k)]
        dist={}
        while heap:
            time,node=heappop(heap)
            if node in dist:
                continue
            dist[node]=time
            for nei,w in graph[node]:
                if nei not in dist:
                    heappush(heap,(time+w,nei))
        return -1 if len(dist)!=n else max(dist.values())