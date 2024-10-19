class Solution:
    def climbStairs(self, n: int) -> int:
        iMinus1 = 1
        iMinus2 = 1

        for i in range(2, n+1): # n+1 because this is number of stairs, that means it not gonna start with 0
            curr = (iMinus1     # either you can come from 1 step prior
                    + iMinus2)  # or you can come from 2 steps prior

                                # for next element
            iMinus2 = iMinus1   # the previous become 2 steps prior
            iMinus1 = curr      # the current becomes 1 step prior
    
        return iMinus1

# At each step, we can reach it either from 1 step prior or 2 step prior. So the ways is the sum of ways to reach those two steps. Remember that n steps doesnt start from 0.

# Time Complexity >> O(n)
# Space Complexity >> O(1)