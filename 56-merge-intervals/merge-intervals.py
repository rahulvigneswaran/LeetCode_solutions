class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        res = []
        intervals.sort(key = lambda a : a[0])
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            if prevInterval[1] >= intervals[i][0]:
                prevInterval = [min(prevInterval[0], intervals[i][0]), max(prevInterval[1], intervals[i][1])]
            else:
                res.append(prevInterval)
                prevInterval = intervals[i]
        res.append(prevInterval)
        return res

# Time complexity >> O(n)
# Space complexity >> O(n)