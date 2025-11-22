class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        for n in nums:
            if counter == 0:
                res = n
            if res == n:
                counter += 1
            else:
                counter -= 1
        return res