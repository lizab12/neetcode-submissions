class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0

        # ✅ Define dfs before using it
        def dfs(r, c):
            # Base case: out of bounds or water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            # Mark this cell as visited
            grid[r][c] = 0

            # Count current cell
            area = 1

            # Explore 4 directions
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        # ✅ Traverse every cell
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxarea = max(maxarea, area)

        return maxarea
