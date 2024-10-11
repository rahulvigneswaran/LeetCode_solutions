class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum