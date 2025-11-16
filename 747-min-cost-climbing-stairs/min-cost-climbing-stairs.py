class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # # recursive brute-force (no memoization)
        # def dfs(node):
        #     if node <= 1:
        #         return cost[node]
            
        #     return cost[node] + min(dfs(node-1), dfs(node-2))
        
        # return min(dfs(len(cost)-1), dfs(len(cost)-2))
        
        # memoization
        # top-down
        dp = [-1]*len(cost)

        def dfs(node):
            if node <= 1:
                return cost[node]

            if dp[node] != -1:
                return dp[node]
            
            cost_at_node = cost[node] + min(dfs(node-1), dfs(node-2))
            dp[node] = cost_at_node

            return cost_at_node

        n = len(cost)
        return min(dfs(n-1), dfs(n-2))