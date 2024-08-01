class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
            
        memory = {}
        for ind in range(len(nums)):
            remain = target - nums[ind]
            ans = memory.get(remain, -1)
            if ans < 0:
                memory[nums[ind]] = ind
            else:
                return [ans, ind]
