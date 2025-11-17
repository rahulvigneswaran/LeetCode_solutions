class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # recursive
        # def dfs(target, coinsLeft):
        #     # base cases
        #     if target == amount:
        #         return 1
        #     if target > amount:
        #         return 0
            
        #     res = 0
        #     for c in range(len(coinsLeft)):
        #         res += dfs(target+coinsLeft[c], coinsLeft[c:])
            
        #     return res
        
        # return dfs(0, coins)

        # memoization
        # memo = {}
        # coins.sort()
        # def dfs(target, coinInd):
        #     # base cases
        #     if target == amount:
        #         return 1
        #     if target > amount or coinInd == len(coins):
        #         return 0
            
        #     if (target, coinInd) in memo:
        #         return memo[(target, coinInd)]

        #     res = 0
        #     for c in range(coinInd, len(coins)):
        #         res += dfs(target+coins[c], c)
            
        #     memo[(target, coinInd)] = res
        #     return res
        
        # return dfs(0, 0)
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][a] != -1:
                return memo[i][a]

            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])

            memo[i][a] = res
            return res

        return dfs(0, amount)