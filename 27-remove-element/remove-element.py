class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        L = 0 
        R = len(nums)-1
        while L <= R:
            if nums[L] == val:
                while nums[R] == val and L < R:
                    R -= 1
                    res+=1
                nums[L], nums[R] = nums[R], nums[L]
                res+=1
                R-=1
            L += 1
        return len(nums) - res
        