class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda a : a[0])
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(prevEnd, intervals[i][1])
                res += 1
        return res

# Time >> O(n)
# Space >> O(1)