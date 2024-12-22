class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if not jewels or not stones:
            return 0
        count = 0
        for jewel in jewels:
            count += stones.count(jewel)
        return count
            