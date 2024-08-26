class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        LongestLength = 0
        for i in nums:
            if not(i-1 in nums):
                Length = 0 
                while (i + Length) in nums:
                    Length += 1
                LongestLength = max(LongestLength, Length)
        return LongestLength
            
        