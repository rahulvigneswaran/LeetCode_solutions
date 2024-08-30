class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find min in log(n) -> do typical BS in log(n) either on left or right
        l, r = 0, len(nums)-1
        
        while l <= r and r < len(nums):
            m = (l+r) // 2
            if nums[m] == target : 
                return m

            if nums[m] >= nums[l]: #belong to left
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1