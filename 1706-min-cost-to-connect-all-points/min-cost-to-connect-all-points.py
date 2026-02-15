class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        N = len(points)
        for i in range(N):
            for j in range(i+1, N):
                dist = abs(points[i][0]- points[j][0]) + abs(points[i][1]- points[j][1])
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        visited = set()
        minHeap = [(0, 0)]
        res = 0
        while len(visited) < N:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += dist
            visited.add(node)
            for nei_dist, nei_node in adjList[node]:
                if nei_node in visited:
                    continue
                heapq.heappush(minHeap, (nei_dist, nei_node))
        return res
        