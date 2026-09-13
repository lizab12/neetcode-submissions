class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        c=0
        i=1
        prev = intervals[0][1]
        while i<(len(intervals)):
            if intervals[i][0]<prev:
                c+=1
            else:
                prev = intervals[i][1]
            i+=1
        return c


        