class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # # recursive brute-force (no memoization)
        # def dfs(node):
        #     if node <= 1:
        #         return cost[node]
            
        #     return cost[node] + min(dfs(node-1), dfs(node-2))
        
        # return min(dfs(len(cost)-1), dfs(len(cost)-2))
        
        # memoization

        # # top-down
        # dp = [-1]*len(cost)

        # def dfs(node):
        #     if node <= 1:
        #         return cost[node]

        #     if dp[node] != -1:
        #         return dp[node]
            
        #     cost_at_node = cost[node] + min(dfs(node-1), dfs(node-2))
        #     dp[node] = cost_at_node

        #     return cost_at_node

        # n = len(cost)
        # return min(dfs(n-1), dfs(n-2))

        # # bottom-up
        # dp = cost
        # n = len(cost)
        # if len(cost) == 2:
        #     return min(cost)

        # for i in range(2, n):
        #     dp[i] = dp[i] + min(dp[i-1], dp[i-2])

        # return min(dp[n-1], dp[n-2])

        # bottom-up space optimized
        Minus1, Minus2 = cost[1], cost[0]
        n = len(cost)
        for i in range(2, n):
            Minus1, Minus2 = cost[i] + min(Minus1, Minus2), Minus1
        
        return min(Minus1, Minus2)
