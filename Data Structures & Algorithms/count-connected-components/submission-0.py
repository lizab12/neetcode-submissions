class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = 0
        adj = {i:[] for i in range(n)}
        visit = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(n):
            visit.add(n)
            for nei in adj[n]:
                if nei not in visit:
                    dfs(nei)
        
        for i in range(n):
            if i in visit:
                continue
            else:
                comp+=1
                dfs(i)
        
        return comp