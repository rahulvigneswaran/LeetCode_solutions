class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        cumNum = 1
        for i in range(len(nums)):
            res[i] *= cumNum 
            cumNum *= nums[i]
        
        cumNum = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= cumNum
            cumNum *= nums[i]
        return res
        
# Time >> O(n)
# Space >> O(n)
        


        