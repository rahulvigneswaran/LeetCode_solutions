class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for i in nums:
            if i - 1 not in numSet:
                consecNum = i
                length = 0
                while consecNum in numSet:
                    length += 1
                    consecNum += 1
                res = max(res, length)
        return res

# create a numSet. Start counting only when the there is no number previous to the current.
# Optimized solution >> Time : O(n). Space : O(n)
        