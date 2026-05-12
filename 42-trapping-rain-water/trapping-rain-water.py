class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        leftMax, rightMax = height[L], height[R]
        res = 0
        while L < R:
            if leftMax <= rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                res += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                res += rightMax - height[R]
        return res