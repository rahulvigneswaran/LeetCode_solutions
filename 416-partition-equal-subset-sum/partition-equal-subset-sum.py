class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # # recursion (no memoization)
        # def dfs(n, targetSum):
        #     if n == len(nums):
        #         return targetSum == 0

        #     return dfs(n+1, targetSum - nums[n]) or dfs(n+1, targetSum)
        
        # if sum(nums) % 2 != 0:
        #     return False
        # return dfs(0, sum(nums)//2)

        # memoization
        # top-down

        if sum(nums) % 2 != 0:
            return False
        
        memo = {}

        def dfs(n, targetSum):
            if n == len(nums):
                return targetSum == 0
            
            if (n, targetSum) not in memo:
                memo[(n, targetSum)] = dfs(n+1, targetSum - nums[n]) or dfs(n+1, targetSum)

            return memo[n, targetSum]
        
        return dfs(0, sum(nums)//2)