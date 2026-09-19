class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0
        s = []

        for i , h in enumerate(heights):
            start = i
            while s and s[-1][1]>h:
                index , height = s.pop()
                m = max(m, height*(i-index))
                start = index
            s.append((start,h))
        
        for i,h in s:
            m = max(m, h*(len(heights)-i) )
        return m
        