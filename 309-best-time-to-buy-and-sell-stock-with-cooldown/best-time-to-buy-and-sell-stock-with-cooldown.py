class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # recursive
        # def dfs(n, canBuy):
        #     if n == len(prices):
        #         return 0

        #     cooldown = dfs(n+1, canBuy)

        #     if canBuy:
        #         profit = dfs(n+1, not canBuy) - prices[n]
        #     else:
        #         profit = dfs(n+2, not canBuy) + prices[n]
            
        #     return max(profit, cooldown)

        # return dfs(0, True)
        # memoization
        memo = {}

        def dfs(n, canBuy):
            if n >= len(prices):
                return 0

            if (n, canBuy) in memo:
                return memo[(n, canBuy)]

            cooldown = dfs(n+1, canBuy)

            if canBuy:
                profit = dfs(n+1, not canBuy) - prices[n]
            else:
                profit = dfs(n+2, not canBuy) + prices[n]
            
            memo[(n, canBuy)] = max(profit, cooldown)
            return memo[(n, canBuy)]

        return dfs(0, True)

        # tabulation
        