class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        while i<=j:
            mid = (i+j)//2
            hrs = 0
            for p in piles:
                hrs += (p + mid - 1) // mid
            if h>=hrs:
                j = mid -1
            else:
                i = mid + 1
        return i
        