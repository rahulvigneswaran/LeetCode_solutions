class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        l, r = 0, 1
        max_profit = 0
        while (l<len(prices) and r<len(prices)):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
                r = l+1
            elif max_profit < diff:
                max_profit = diff
                r += 1
            else:
                r += 1
        return max_profit
