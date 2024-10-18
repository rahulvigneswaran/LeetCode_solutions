class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float("inf")
        dpMax = 1
        dpMin = 1

        for n in nums:
            if n == 0:
                dpMax, dpMin = 1, 1
                res = max(res, n)
            else:
                productWithMax = dpMax * n
                productWithMin = dpMin * n
                dpMax = max(productWithMax, productWithMin, n)
                dpMin = min(productWithMax, productWithMin, n)
                res = max(res, dpMax)
        return res


# Brute Force solution >> Just compare everything with everything.
# Time complexity >> O(n^2)
# Space complexity >> O(1)

# Optimized solution >> There are 4 edges cases. 1) All +ve : Just multply everything. 2) Mixed -ve +ve : If the current number is +ve, the max is the max of previous * current. But if current number is -ve, the max is the min (because this would have the largest absolute value) of previous multiplied by the current number. 3) There is a ZERO : If zero exists, just reset the dp values to 1, so it wont affect the next number's decision. 4) If both the max and min from previous is -ve: When checking max and min, compare with current number too. 
# Time complexity >> O(n)
# Space complexity >> O(1)