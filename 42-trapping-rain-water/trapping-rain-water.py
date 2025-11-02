class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        res = 0
        leftMax, rightMax = height[0], height[-1]
        L, R = 0, len(height)-1
        
        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L]) # to prevent negative
                res += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R]) # to prevent negative
                res += rightMax - height[R]
        return res

