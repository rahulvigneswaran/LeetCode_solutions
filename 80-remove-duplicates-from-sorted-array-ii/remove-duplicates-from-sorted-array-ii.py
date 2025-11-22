class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0] - 1
        uniq_ind = 0
        for i in range(len(nums)):
            if nums[i] != prev: # start of uniq
                nums[uniq_ind] = nums[i]
                prev = nums[i]
                cand_count = 1
                uniq_ind += 1
                flag = True
            elif flag:
                nums[uniq_ind] = nums[i]
                uniq_ind += 1
                flag = False
        return uniq_ind


            
