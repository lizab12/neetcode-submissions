class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        d1 = set()
        d2 = set()

        res = []
        board = [["."]*n for i in range(n)]

        def dfs(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in d1 or (r-c) in d2:
                    continue
                col.add(c)
                d1.add(r+c)
                d2.add(r-c)
                board[r][c] = "Q"

                dfs(r+1)

                col.remove(c)
                d1.remove(r+c)
                d2.remove(r-c)
                board[r][c] = "."

        dfs(0)
        return res
