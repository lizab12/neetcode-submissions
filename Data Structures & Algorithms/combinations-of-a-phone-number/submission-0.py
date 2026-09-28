class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        h = {}
        h["2"]="abc"
        h["3"]="def"
        h["4"]="ghi"
        h["5"]="jkl"
        h["6"]="mno"
        h["7"]="pqrs"
        h["8"]="tuv"
        h["9"]="wxyz"

        def dfs(i, cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for c in h[digits[i]]:
                dfs(i+1, cur+c)
        if digits:
            dfs(0,"")

        return res        