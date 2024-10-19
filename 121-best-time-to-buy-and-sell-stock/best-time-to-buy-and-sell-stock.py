class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # base
        if len(prices) < 2:
            return 0
        
        L = 0
        R = 1
        maxProfit = 0
        while L < R and R < len(prices):
            if prices[L] > prices[R]:
                L=R
            else:
                maxProfit = max(maxProfit, prices[R]-prices[L])
            R+=1
        return maxProfit

# Buy low, sell high. Whenever right is smalller than left, make L=R. If right is greater than left, increment R.

# Time complexity >> o(n)
# Space complexity >> O(1)


