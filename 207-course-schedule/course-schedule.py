class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            adjList[i].append(j)
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if adjList[node] == []:
                return True
            
            visited.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            adjList[node] = []
            return True

        for root in range(numCourses):
            if not dfs(root):
                return False
        return True
# Do DFS. Create adjList. If visited, its loop. False. Remove from visited after fully doing DFS and also make it [].
# Optimized solution >> Time : O(n+e). Space : O(n). n is number of nodes.