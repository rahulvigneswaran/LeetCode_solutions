class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        SolutionSet = []
        for i, l0 in enumerate(nums):
            if l0 > 0:
                break
            if i > 0 and (l0 == nums[i-1]):
                continue
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                ThreeSum = l0 + nums[l] + nums[r]
                if ThreeSum > 0:
                    r-=1
                elif ThreeSum < 0 :
                    l+=1
                else:
                    SolutionSet.append([l0, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return SolutionSet


