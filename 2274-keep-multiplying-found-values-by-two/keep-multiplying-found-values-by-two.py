class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        # naive
        while True:
            if original in nums:
                original *= 2
            else:
                return original