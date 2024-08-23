class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom-up
        if n < 4:
            return n
        cache = [2,3]
        for i in range(4, n+1):
            new = cache[0] + cache[1]
            cache[0], cache[1] = cache[1], new
        
        return cache[-1]