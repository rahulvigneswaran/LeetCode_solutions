class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = nums[0]
        for i in nums[1:]:
            out = out^i
        
        for i in range(len(nums)+1):
            out = out^i
        
        return out