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

        # # memo
        # memo = {}
        # # dfs
        # N = len(prices)
        # def dfs(ind, is_buy):
        #     if ind >= N:
        #         return 0
            
        #     if (ind, is_buy) in memo:
        #         return memo[(ind, is_buy)]

        #     # skip
        #     max_p = dfs(ind+1, is_buy)

        #     # buy
        #     if is_buy:
        #         p = dfs(ind+1, False) - prices[ind]
        #         max_p = max(max_p, p)
        #     else:
        #         p = dfs(ind+2, True) + prices[ind]
        #         max_p = max(max_p, p)
            
        #     memo[(ind, is_buy)] = max_p

        #     return max_p

        
        # return dfs(0, True)

        # # Tab
        # tab = defaultdict(int)
        # # dfs
        # N = len(prices)

        # for ind in range(N-1, -1, -1):
        #     # 1: True, 0: False
        #     # if in buy
        #     tab[(ind, 1)] = max(tab[(ind+1, 1)], tab[(ind+1, 0)] - prices[ind])

        #     # if in sell
        #     tab[(ind, 0)] = max(tab[(ind+1, 0)], tab[(ind+2, 1)] + prices[ind])
        
        # return tab[(0, 1)] 

        # tab (space optimized)
        tab_1 = [0, 0]
        tab_2 = [0, 0]
        N = len(prices)

        for ind in range(N-1, -1, -1):
            curr = [0, 0]

            curr[1] = max(tab_1[1], tab_1[0] - prices[ind])
            curr[0] = max(tab_1[0], tab_2[1] + prices[ind])

            tab_1, tab_2 = curr, tab_1
        
        return tab_1[1]

        

