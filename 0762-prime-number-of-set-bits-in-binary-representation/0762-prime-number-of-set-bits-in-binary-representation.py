class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def is_prime(num):
            if num < 2:
                return False
            
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    return False
            return True
        count = 0
        
        for num in range(left, right+1):
            set_bits = bin(num).count('1')
            if is_prime(set_bits):
                count += 1
        return count
        