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
        
        # # top-down

        # if sum(nums) % 2 != 0:
        #     return False
        
        # memo = {}

        # def dfs(n, targetSum):
        #     if n == len(nums):
        #         return targetSum == 0
            
        #     if (n, targetSum) not in memo:
        #         memo[(n, targetSum)] = dfs(n+1, targetSum - nums[n]) or dfs(n+1, targetSum)

        #     return memo[n, targetSum]
        
        # return dfs(0, sum(nums)//2)


        # bottom-up

        # edge cases
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        
        # grid
        tab = [[False]*(target + 1) for _ in range(len(nums)+1)]

        # prefill base conditions
        for i in range(len(nums)+1):
            tab[i][0] = True

        # iteration
        for n in range(1, len(nums)+1):
            for capacity in range(1, target+1): 
                if nums[n-1] <= capacity:
                    tab[n][capacity] = tab[n-1][capacity] or tab[n-1][capacity - nums[n-1]]
                else:
                    tab[n][capacity] = tab[n-1][capacity]
                
        return tab[len(nums)][target]


                     