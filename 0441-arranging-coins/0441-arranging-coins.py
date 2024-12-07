class Solution:
    # def arrangeCoins(self, n: int) -> int:
    #     remaining_coin = n
    #     for i in range(1, n+1):
    #         if remaining_coin > i:
    #             remaining_coin -= i
    #         elif remaining_coin == i:
    #             return i
    #         else:
    #             return i-1
    #     return -1
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            curr_sum = mid * (mid + 1) // 2
            if curr_sum == n:
                return mid
            elif curr_sum < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
