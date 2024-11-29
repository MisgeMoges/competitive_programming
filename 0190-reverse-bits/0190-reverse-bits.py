class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_sum = 0
        
        for i in range(32):
            bit = n & 1
            reversed_sum = (reversed_sum << 1) | bit
            n >>= 1
        return reversed_sum