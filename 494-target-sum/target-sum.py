class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # recursion
        # def dfs(n, total):
        #     #base case
        #     if n == len(nums):
        #         return int(total == target)
            
        #     # recursion statement
        #     res = dfs(n+1, total+nums[n]) + dfs(n+1, total-nums[n])

        #     return res
        
        # return dfs(0, 0)

        # memoization
        memo = {}
        def dfs(n, total):
            #base case
            if n == len(nums):
                return int(total == target)
            
            if (n, total) in memo:
                return memo[(n,total)]
            
            # recursion statement
            res = dfs(n+1, total+nums[n]) + dfs(n+1, total-nums[n])

            memo[(n,total)] = res
            return res
        
        return dfs(0, 0)
        