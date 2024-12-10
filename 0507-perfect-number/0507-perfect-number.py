class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        divisor = 2
        divisor_sum = 1
        while divisor <= (int(math.sqrt(num))):
            if num % divisor == 0:
                divisor_sum += divisor
                if divisor != num//divisor:
                    divisor_sum += num//divisor
            
            divisor += 1
       
        return divisor_sum == num