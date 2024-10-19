class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0: #that is using the coin c is doesnt exceed the amount a
                    dp[a] = min(dp[a], 1+dp[a-c]) # that is, either dont use coin c or use coin c (hence the 1) and use the dp at location of a-c.
        
        return dp[amount] if dp[amount] != amount+1 else -1

# we have to calculate the minimum coin for all amount ranging from 0 to the amount. We will check for all coins at each index and keep the minimum of whether to use the coin or not to use. If we use the coin, then we do 1+dp[a-c]. Basically dp[a] = min(dp[a], 1+dp[a-c])

# Time complexity >> O(n*m)
# Space complexity >> O(n)