class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]
        
        positions = [i for i, bit in enumerate(binary_str) if bit == "1"]
        
        if len(positions) < 2:
            return 0
        
        max_gap = max(positions[i]-positions[i-1] for i in range(1, len(positions)))
        
        return max_gap