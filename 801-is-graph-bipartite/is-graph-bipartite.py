class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # no color: None, colors: 0, 1
        colors = [None]*len(graph)


        def dfs(node, color):
            # if not colored, color it 
            if colors[node] is None:
                colors[node] = color
            
            # go through children
            for child in graph[node]:
                
                # if not colored, dfs
                if colors[child] is None:
                    if not(dfs(child, 1 - color)):
                        return False
                
                # if colored, check
                else:
                    if colors[child] == colors[node]:
                        return False
            
            return True

        # there can be more than 1 disconnected graphs
        for i in range(len(graph)):
            if colors[i] is None:
                if not(dfs(i, 0)):
                    return False
        
        return True