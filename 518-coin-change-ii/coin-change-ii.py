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
        memo = {}
        def helper(ind, total):
            if amount == total:
                return 1
            if total > amount or ind == len(coins):
                return 0

            if (ind, total) in memo:
                return memo[(ind, total)]

            # include
            a = helper(ind, total + coins[ind])

            # skip
            b = helper(ind+1, total)
            
            memo[(ind, total)] = a + b
            return a + b
        
        return helper(0, 0)