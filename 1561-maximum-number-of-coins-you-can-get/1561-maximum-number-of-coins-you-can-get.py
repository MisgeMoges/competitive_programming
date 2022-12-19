class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        j, i = 0, len(piles)-1
        total = 0
        while j < i:
            total += piles[i-1]
            i -= 2
            j += 1
        return total