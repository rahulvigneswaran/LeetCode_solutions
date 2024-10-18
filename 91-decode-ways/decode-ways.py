class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if (i+1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]

# Go from last to first. The sub problem is ways the next index can be decoded. If its single, then the values is same as i+1. If its double, then the values is i+1 and i+2. For double, use the first and second digit to narrow down the comparison.