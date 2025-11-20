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
            
        #     # recursion statement
        #     res = dfs(target, coinInd + 1) + dfs(target+coins[coinInd], coinInd)
            
        #     memo[(target, coinInd)] = res
        #     return res
        
        # return dfs(0, 0)

        # tabulation

        # dims
        COLS = amount + 1
        ROWS = len(coins) + 1
        # table
        tab = [[0]*COLS for _ in range(ROWS) ]

        # base conditions
        for i in range(ROWS):
            tab[i][COLS-1] = 1

        # iterations last -> first

        for coinInd in range(ROWS - 2, -1, -1):
            for target in range(COLS - 1, -1, -1):
                rightVal = 0
                right = target+coins[coinInd]
                if right <= COLS-1:
                    rightVal = tab[coinInd][right]
                tab[coinInd][target] = tab[coinInd + 1][target] + rightVal
        
        return tab[0][0]
        