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
        # total = sum(nums)
        # n = len(nums)

        # # edge cases
        # if total % 2 != 0:
        #     return False

        # target = total // 2
        
        # # grid
        # tab = [[False]*(target + 1) for _ in range(n+1)]

        # # prefill base conditions
        # for i in range(n+1):
        #     tab[i][0] = True

        # # iteration
        # for i in range(1, n+1):
        #     for j in range(1, target+1): 
        #         if nums[i-1] <= j:
        #             tab[i][j] = tab[i-1][j] or tab[i-1][j - nums[i-1]]
        #         else:
        #             tab[i][j] = tab[i-1][j]
                
        # return tab[n][target]


        # bottom-up (space optimized)
        total = sum(nums)
        n = len(nums)

        # edge cases
        if total % 2 != 0:
            return False

        target = total // 2
        
        # grid
        prev = [False]*(target + 1)
        

        # prefill base conditions
        prev[0] = True

        # iteration
        for i in range(1, n+1):
            curr = [False]*(target + 1)
            curr[0] = True
            for j in range(1, target+1): 
                if nums[i-1] <= j:
                    curr[j] = prev[j] or prev[j - nums[i-1]]
                else:
                    curr[j] = prev[j]
            prev = curr
                
        return curr[target]

        


                     