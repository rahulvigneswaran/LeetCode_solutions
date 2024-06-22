class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set(nums)
        return len(uniques) != len(nums)