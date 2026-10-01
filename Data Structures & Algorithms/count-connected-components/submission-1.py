class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        c = 0
        h = {i:[] for i in range(n)}
        for a,b in edges:
            h[a].append(b)
            h[b].append(a)
        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in h[i]:
                dfs(j)

        for i in range(n):
            if i not in visited:
                c+=1
                dfs(i)
        
        return c
        