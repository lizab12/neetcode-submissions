class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                num = board[r][c]
                ix = (r//3)*3+(c//3)
                if num in rows[r] or num in cols[c] or num in squares[ix]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[ix].add(num)
        return True