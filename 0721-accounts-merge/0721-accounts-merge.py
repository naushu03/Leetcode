class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        parent=list(range(n))
        rank=[1]*n
        def find(x):
            p=parent[x]
            while parent[p]!=p:
                parent[p]=parent[parent[p]]
                p=parent[p]
            return p
        def union(a,b):
            pa,pb=find(a),find(b)
            if pa==pb:
                return
            if rank[pa]<rank[pb]:
                parent[pa]=pb
                rank[pb]+=rank[pa]
            else:
                parent[pb]=pa
                rank[pa]+=rank[pb]
        d={}
        for i in range(len(accounts)):
            for j in accounts[i][1:]:
                if j not in d:
                    d[j]=i
                else:
                    union(d[j],i)
        graph=defaultdict(list)
        for i,j in d.items():
            w=find(j)
            graph[w].append(i)
        op=[]
        for i,j in graph.items():
            op.append([accounts[i][0]])
            op[-1].extend(sorted(j))
        return op