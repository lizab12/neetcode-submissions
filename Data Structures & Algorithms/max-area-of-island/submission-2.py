class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        l = len(grid[0])
        m = 0

        def dfs(i,j):
            if i>=r or j>=l or i<0 or j<0 or grid[i][j]==0:
                return 0
            
            grid[i][j]=0
            return ( 1+ dfs(i-1,j) + dfs(i+1,j)
            + dfs(i,j-1)
           + dfs(i,j+1))

        for i in range(r):
            for j in range(l):
                if grid[i][j]==1:
                    n = dfs(i,j)
                    if n>m:
                        m= n
        return m
        