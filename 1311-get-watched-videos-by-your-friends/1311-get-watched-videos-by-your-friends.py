class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q,visited=deque([id]),{id}
        for i in range(level):
            for _ in range(len(q)):
                x=q.popleft()
                for nei in friends[x]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        d={}
        for p in q:
            for videos in watchedVideos[p]:
                d[videos]=d.get(videos,0)+1
        return sorted(d.keys(),key=lambda x:(d[x],x))