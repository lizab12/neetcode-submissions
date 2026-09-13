class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        if m<n:
            m,n = n,m
        res  = temp = 1
        for i in range(m,m+n-1):
            res= res*i
            res= res/temp
            temp+=1
        return int(res)

        