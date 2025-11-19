class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # naive
        nums.sort()
        for n in nums:
            if n == original:
                original *= 2
        return original

        # hash set
        # L = 0
        # while L < len(nums):
        #     for i in range(L, len(nums)):
        #         if nums[i] == original:
        #             original *= 2
        #             L = i + 1
        #         elif nums[i] > original:
        #             break                    

        # return original