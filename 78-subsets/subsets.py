class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # dfs
        def helper(ind):

            if ind >= len(nums):
                res.append(subset.copy())
                return
            
            
            subset.append(nums[ind])
            helper(ind + 1)
            subset.pop()
            helper(ind + 1)
        
        helper(0)
        
        return res