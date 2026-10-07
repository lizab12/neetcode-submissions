class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            longest = 1

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < rows and
                    0 <= nj < cols and
                    matrix[ni][nj] > matrix[i][j]
                ):
                    longest = max(longest, 1 + dfs(ni, nj))

            memo[(i, j)] = longest
            return longest

        ans = 0

        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))

        return ans