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
        # memo = {}
        # def dfs(n, total):
        #     #base case
        #     if n == len(nums):
        #         return int(total == target)
            
        #     if (n, total) in memo:
        #         return memo[(n,total)]
            
        #     # recursion statement
        #     res = dfs(n+1, total+nums[n]) + dfs(n+1, total-nums[n])

        #     memo[(n,total)] = res
        #     return res
        
        # return dfs(0, 0)
        
        # Tabulation
        # # dims
        # ROWS = len(nums) + 1
        # COLS = sum(nums) + 1 #target + 1
        
        # # table
        # tab = [defaultdict(int) for _ in range(ROWS)]

        # # base condition
        # # for r in range(ROWS):
        # tab[len(nums)][target] = 1

        # # ROWS: last -> 0
        # # COLS: last -> 0
        # for r in range(ROWS-2, -1, -1):
        #     for c in range(COLS, -COLS, -1):
        #         tab[r][c] = tab[r+1][c + nums[r]] + tab[r+1][c - nums[r]]
        
        # return tab[0][0]

        # Tabulation (Space Optimized)
        # dims
        ROWS = len(nums) + 1
        COLS = sum(nums) + 1 #target + 1
        
        # table
        prev = defaultdict(int)

        # base condition
        # for r in range(ROWS):
        prev[target] = 1

        # ROWS: last -> 0
        # COLS: last -> 0
        for r in range(ROWS-2, -1, -1):
            curr = defaultdict(int)
            for c in range(COLS, -COLS, -1):
                curr[c] = prev[c + nums[r]] + prev[c - nums[r]]
            prev = curr
        
        return curr[0]