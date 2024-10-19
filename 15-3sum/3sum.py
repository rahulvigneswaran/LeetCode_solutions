class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for n1, val in enumerate(nums):
            if n1 > 0 and nums[n1] == nums[n1-1]:
                continue
            
            L = n1 + 1
            R = len(nums) - 1
            while L < R:
                addedSum = nums[n1] + nums[L] + nums[R]
                if addedSum > 0:
                    R-=1
                elif addedSum < 0:
                    L+=1
                else:
                    res.append([nums[n1], nums[L], nums[R]])
                    L+=1
                    while nums[L] == nums[L-1] and L < R:
                        L+=1
        return res

# Not a TwoSum problem with the first number fixed. This cant have duplicates. Sort the array. Fix the first number. Dont use the first number if it is same as the previous. This means we already used this to find TwoSum. Now for the next two numbers, we can use typical twoSum but we can do better by not using the extra space for hash. We exploit the sorted property and use two pointers. Increase left if <0, decrease right if >0. Here to iterate left if its a duplicate.

# Time complexity >> O(n^2)
# Space complexity >> O(1)