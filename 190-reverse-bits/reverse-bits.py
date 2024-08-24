class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            bit = (n >> i) & 1
            out = out | (bit << 31-i)
        return out