class Solution:
    def maxArea(self, height: List[int]) -> int:
        MaxArea = -1
        l, r = 0, len(height) - 1

        while l < r:
            Area = (r-l)*min(height[l], height[r])
            MaxArea = max(MaxArea, Area)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return MaxArea