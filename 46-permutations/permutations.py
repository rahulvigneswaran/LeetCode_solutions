class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def helper(leftover_nums):
            if not leftover_nums:
                res.append(subset.copy())
                return 
                        
            for i in range(len(leftover_nums)):            
                num = leftover_nums.pop(i)
                subset.append(num)
                helper(leftover_nums)
                subset.pop()
                leftover_nums.insert(i, num)
        
        helper(nums)
        
        return res
            