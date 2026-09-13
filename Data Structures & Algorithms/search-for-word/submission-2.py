class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,m):
            if m == len(word):
                return True
            if i<0 or j<0 or i>x-1 or j>y-1 or board[i][j]!=word[m]: 
                return False
            temp = board[i][j]
            board[i][j]='#'
            there = dfs(i,j+1,m+1) or dfs(i,j-1,m+1) or dfs(i+1,j,m+1) or dfs(i-1,j,m+1)
            board[i][j]=temp
            return there
        x = len(board)
        y = len(board[0])
        m = 0
        for i in range(x):
            for j in range(y):
                if word[0]==board[i][j]:
                    found = dfs(i,j,m)
                    if found:
                        return True
        return False


    
        