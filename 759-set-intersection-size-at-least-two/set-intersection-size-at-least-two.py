class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sort
        intervals.sort(key = lambda x: (x[1], -x[0]))

        p1 = -1
        p2 = -1
        ans = 0

        for start, end in intervals:
            if start > p2:
                ans += 2
                p1 = end-1
                p2 = end
            elif start > p1:
                ans += 1
                p1 = p2
                p2 = end
        
        return ans
