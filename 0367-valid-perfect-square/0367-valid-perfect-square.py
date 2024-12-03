class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i*i <= num:
            result = i*i
            if result == num:
                return True
            i+=1
        return False
        
        