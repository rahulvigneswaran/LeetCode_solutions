class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # naive
        # # dfs
        # N = len(prices)
        # def dfs(ind, is_buy):
        #     if ind >= N:
        #         return 0
            
        #     # skip
        #     max_p = dfs(ind+1, is_buy)

        #     # buy
        #     if is_buy:
        #         p = dfs(ind+1, False) - prices[ind]
        #         max_p = max(max_p, p)
        #     else:
        #         p = dfs(ind+2, True) + prices[ind]
        #         max_p = max(max_p, p)
            
        #     return max_p

        
        # return dfs(0, True)

        # memo
        memo = {}
        # dfs
        N = len(prices)
        def dfs(ind, is_buy):
            if ind >= N:
                return 0
            
            if (ind, is_buy) in memo:
                return memo[(ind, is_buy)]

            # skip
            max_p = dfs(ind+1, is_buy)

            # buy
            if is_buy:
                p = dfs(ind+1, False) - prices[ind]
                max_p = max(max_p, p)
            else:
                p = dfs(ind+2, True) + prices[ind]
                max_p = max(max_p, p)
            
            memo[(ind, is_buy)] = max_p
            
            return max_p

        
        return dfs(0, True)
        

