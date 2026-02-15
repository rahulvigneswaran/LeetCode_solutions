class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = {}

        adjList = defaultdict(list)
        
        for u, v, w in times:
            adjList[u].append((w, v))
        
        minheap = [(0, k)]

        while minheap:
            w, v = heapq.heappop(minheap)
            if v in shortest:
                continue
            shortest[v] = w
            for (nei_w, nei_v) in adjList[v]:
                heapq.heappush(minheap, (nei_w + w, nei_v))
        res = max(shortest.values())
        return res if (res > 0 and len(shortest) == n) else -1
        