class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # naive
        # nums.sort()
        # for n in nums:
        #     if n == original:
        #         original *= 2
        # return original

        # hash set
        nums = set(nums)
        while original in nums:
            original *= 2
        return original