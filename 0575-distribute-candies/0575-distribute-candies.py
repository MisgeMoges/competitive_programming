class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_type = set()
        for i in range(len(candyType)):
            if candyType[i] not in candy_type:
                candy_type.add(candyType[i])
            if len(candyType)//2 < len(candy_type):
                return len(candyType)//2
        return len(candy_type)