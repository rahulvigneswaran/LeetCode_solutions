class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def helper(ind):
            if ind >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[ind])
            helper(ind + 1)
            subset.pop()

            while ind + 1 < len(nums) and nums[ind] == nums[ind+1]:
                ind += 1
            helper(ind + 1)
        
        helper(0)
        return res