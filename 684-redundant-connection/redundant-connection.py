class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union find

        rank = [1]*(len(edges) + 1)
        pr = [i for i in range(len(edges) + 1)] # since there is one redundant node, #nodes = #edges

        # to find the parent
        def find(n):
            if pr[n] != n:
                pr[n] = find(pr[n])
            return pr[n] 

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # if same parent, then loop
            if p1 == p2:
                return False
            
            # if not, same parent, then add it to the union-find tree
            # whichever has the highest rank will become the grandparent and its rank increased
            elif rank[p1] > rank[p2]:
                pr[p2] = p1
                rank[p1] += rank[p2]
            else:
                pr[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for i, j in edges:
            if not(union(i, j)):
                return [i, j]


        