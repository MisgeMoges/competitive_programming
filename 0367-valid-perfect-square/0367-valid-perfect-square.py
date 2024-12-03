class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # i = 1
        # while i*i <= num:
        #     result = i*i
        #     if result == num:
        #         return True
        #     i+=1
        if num < 1:
            return False
        
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        
        