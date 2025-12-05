class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        leftSum = nums[0]
        rightSum = sum(nums[1:])

        res = 0
        for n in nums[:-1]:
            diff = leftSum - rightSum
            if diff % 2 == 0:
                res +=1
            
            leftSum += n
            rightSum -= n
        return res


        # 0  36 = even
        # 10 26 = even
        # 20 16 = even
        # 23 13 = even
        # 30 30 = even
        # 36 0 

        