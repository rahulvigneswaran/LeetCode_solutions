class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*i for i in nums]
        heapq.heapify(nums)

        for _ in range(k):
            res = heapq.heappop(nums)
        return -1*res
        