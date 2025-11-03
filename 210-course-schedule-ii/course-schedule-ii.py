class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        res = [] # set is unordered
        visited = set()
        cycle = set()

        #dfs
        def helper(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            for child in adjList[node]:
                if not(helper(child)):
                    return False
            
            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        

        for i in range(numCourses):
            if not(helper(i)):
                return []
        return res