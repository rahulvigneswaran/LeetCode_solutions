class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # # naive recursion
        # def helper(i):
        #     if i >= len(nums):
        #         return 0

        #     skip = helper(i+1)
        #     noskip = helper(i+2) + nums[i]

        #     return max(skip, noskip)
        
        # return helper(0)

        # memo
        # memo = {}
        # def helper(i):
        #     if i >= len(nums):
        #         return 0

        #     if i in memo:
        #         return memo [i]
        #     skip = helper(i+1)
        #     noskip = helper(i+2) + nums[i]
        #     memo[i] = max(skip, noskip)
        #     return memo[i]
        
        # return helper(0)

        # tab
        tab = [0]*(len(nums)+2)

        for i in range(len(nums)-1, -1, -1):
            tab[i] = max(tab[i+1], tab[i+2]+nums[i])
        
        return tab[0]

        # tab (space optimized)
        num2, num1 = 0, 0

        for i in range(len(nums)-1, -1, -1):
            num1, num2 = max(num1, num2+nums[i]), num1
        return num1