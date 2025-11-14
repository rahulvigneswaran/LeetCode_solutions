class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # to find the parent
        par = [i for i in range(len(edges)+1)]

        # each edge can have two parents. for (a, b), either parent of a or parent of b. So we should choose the parent with the greated rank
        rank = [1]*(len(edges) + 1)
        
        # finding the topmost parent
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # if same parent, then cycle
            if p1 == p2:
                return False
            
            # if not the same parent, then put under that parent with the highest rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        
        for i, j in edges:
            if not(union(i, j)):
                return [i, j]