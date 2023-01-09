class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = 1
        def inner(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            output = self.myPow(x*x, n//2)
            return x*output if n%2 else output
        
        output =  inner(x, abs(n))
        return output if n >= 0 else 1/output
    