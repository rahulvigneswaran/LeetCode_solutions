class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        CumNum = 1
        for i in range(len(nums)-1):
            CumNum *= nums[i] 
            res[i+1] *= CumNum
        
        CumNum = 1
        for i in range(len(nums)-1, 0, -1):
            CumNum *= nums[i]
            res[i-1] *= CumNum
        
        return res

        