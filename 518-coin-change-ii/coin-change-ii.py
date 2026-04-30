class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # naive recursion
        # def helper(ind, total):
        #     if amount == total:
        #         return 1
        #     if total > amount or ind == len(coins):
        #         return 0

        #     # include
        #     a = helper(ind, total + coins[ind])

        #     # skip
        #     b = helper(ind+1, total)

        #     return a + b
        
        # return helper(0, 0)
        
        # memo
        # memo = {}
        # def helper(ind, total):
        #     if amount == total:
        #         return 1
        #     if total > amount or ind == len(coins):
        #         return 0

        #     if (ind, total) in memo:
        #         return memo[(ind, total)]

        #     # include
        #     a = helper(ind, total + coins[ind])

        #     # skip
        #     b = helper(ind+1, total)
            
        #     memo[(ind, total)] = a + b
        #     return a + b
        
        # return helper(0, 0)

        # tab 
        tab = [[0]*(amount + 1) for _ in range(len(coins)+1)]

        # base case
        for ind in range(len(coins)+1):
            tab[ind][amount] = 1

        for ind in range(len(coins)-1, -1, -1):
            for total in range(amount, -1, -1):

                include = 0
                if total + coins[ind] <= amount:
                    include = tab[ind][total + coins[ind]]

                skip = 0
                skip = tab[ind+1][total]

                tab[ind][total] = include + skip        
        return tab[0][0]