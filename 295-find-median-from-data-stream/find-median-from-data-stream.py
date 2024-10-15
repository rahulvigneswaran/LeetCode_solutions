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


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()