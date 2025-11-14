class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        dp = {}

        def dfs(L, R):
            if L > R:
                return 0
            
            if (L, R) in dp:
                return dp[(L, R)]

            dp[(L, R)] = 0
            for i in range(L, R+1):
                coins = nums[L-1] * nums[i] * nums[R+1]
                coins += dfs(L, i-1) + dfs(i+1, R)
                dp[(L, R)] = max(dp[L, R], coins)
            
            return dp[(L, R)]
        
        return dfs(1, len(nums)-2)