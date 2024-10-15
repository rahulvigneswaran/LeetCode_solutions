class MedianFinder:

    def __init__(self):
        self.left = []  #max heap
        self.right = [] #min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -1*num)

        # left val is greater than right
        if (self.left and self.right
            and -1*self.left[0] > self.right[0]):
            val = -1*heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        # len of left is large
        if len(self.left) > len(self.right) + 1:
            val = -1*heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -1*val)
        
    def findMedian(self) -> float:
        
        if len(self.left) > len(self.right):
            return -1*self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (-1*self.left[0] + self.right[0]) / 2

# Brute Force : Whenever you insert, search and place it in correct sorted positiion.
# Better : Use two heaps. Max heap (multiply by -1) for left and min heap for right. Always insert to the left heap. Then work out the edge cases. left and right should have equal (or +1) elements. Left should always be lesser than right. heapq.heappush(arr, val), heapq.heappop(arr), arr[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()