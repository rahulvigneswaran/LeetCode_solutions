class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy
        res = 0 
        L = R = 0

        while R < len(nums) - 1:
            farthest = L
            for i in range(L, R+1):
                farthest = max(farthest, i + nums[i])
            L = R + 1
            R = farthest
            res += 1
        
        return res
        