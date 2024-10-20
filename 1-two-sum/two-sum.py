class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preDict = {}

        for ind, n in enumerate(nums):
            diff = target - n
            if diff in preDict:
                return [preDict[diff], ind]
            else:
                preDict[n] = ind
        return None

# Time complexity >> O(n)
# Space complexity >> O(n)