class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq_ind = 0
        prev = nums[0] - 1
        for i in range(len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                nums[uniq_ind] = nums[i]
                uniq_ind += 1
        return uniq_ind 