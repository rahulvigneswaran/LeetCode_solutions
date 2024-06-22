class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}    # num: ind
        for ind, num in enumerate(nums):
            diff = target - num
            if prevmap.get(diff, -1) >= 0:
                return [prevmap[diff], ind]
            prevmap[num] = ind
                
        