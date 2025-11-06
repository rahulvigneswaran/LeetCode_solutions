class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #dfs
        def helper(ind, subset):
            if ind >= len(nums):
                res.append(subset)
                return

            helper(ind+1, subset)
            helper(ind+1, subset + [nums[ind]])
        
        helper(0, [])
        return res