class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = -1*heapq.heappop(stones)
            b = -1*heapq.heappop(stones)

            diff = a - b
            if diff > 0:
                heapq.heappush(stones, -1*diff)
        return 0 if len(stones) == 0 else -1*stones[0]
