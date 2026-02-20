class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (math.sqrt(x**2 + y**2), x, y))
        
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append((x, y))
        return res