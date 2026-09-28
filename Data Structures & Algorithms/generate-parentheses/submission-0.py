class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(openn,close):
            if openn==n and close == n:
                res.append("".join(stack))
            if openn<n:
                stack.append("(")
                dfs(openn+1,close)
                stack.pop()
            if close<openn:
                stack.append(")")
                dfs(openn,close+1)
                stack.pop()
        
        dfs(0,0)
        return res
            
        