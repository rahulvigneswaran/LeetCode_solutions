class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        # naive
        while True:
            if original in nums:
                original *= 2
            else:
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