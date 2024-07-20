class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        if len(nums) == 2:
            return [0,1]
            
        for ind, num in enumerate(nums):
            ind_pair = memory.get(target - num, -1)
            if ind_pair >=0 :
                return [ind, ind_pair]
            else:
                memory[num] = ind
