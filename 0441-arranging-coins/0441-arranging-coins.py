class Solution:
    def arrangeCoins(self, n: int) -> int:
        remaining_coin = n
        for i in range(1, n+1):
            if remaining_coin > i:
                remaining_coin -= i
            elif remaining_coin == i:
                return i
            else:
                return i-1
        return -1