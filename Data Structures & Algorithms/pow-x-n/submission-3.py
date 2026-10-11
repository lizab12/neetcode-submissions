class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x,n):
            #base case:
            if n==0:
                return 1
            #what to do with the current node
            half=fastPow(x, n//2)
            if n%2==0:
                return half*half
            else:
                return half*half*x
        res=fastPow(x,abs(n))
        if n>=0:
            return res
        else:
            return 1/res