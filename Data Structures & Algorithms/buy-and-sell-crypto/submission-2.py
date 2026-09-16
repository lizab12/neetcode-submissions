class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        profit = 0
        for i in prices:
            if i<m:
                m = i
            p = i - m
            if p>profit:
                profit = p
        return profit