class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        graph=defaultdict(list)
        for i in range(len(routes)):
            for x in routes[i]:
                graph[x].append(i)
        visitedStops,visitedBus,q={source},set(),deque()
        q.append((source,0))
        while q:
            stops,bus=q.popleft()
            for nei in graph[stops]:
                if nei not in visitedBus:
                    visitedBus.add(nei)
                    for x in routes[nei]:
                        if x==target:
                            return bus+1
                        if x not in visitedStops:
                            visitedStops.add(x)
                            q.append((x,bus+1))
        return -1
