class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        res = 0
        
        maxVal = float("-inf")
        for l in height:
            if l > maxVal:
                maxVal = l
            leftMax.append(maxVal)
        
        maxVal = float("-inf")
        for ind in range(len(height)-1, -1, -1):
            r = height[ind]
            if r > maxVal:
                maxVal = r
            rightMax.append(maxVal)
        
        for ind in range(len(height)):
            res += max(0, min(leftMax[ind], rightMax[len(rightMax)-ind-1]) - height[ind])
        
        return res