class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = 1
        def inner(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            output = self.myPow(x, n//2)
            output *= output
            
            if n%2 ==  1:
                output *= x
            return output
        if n < 0:
            n = -n
            x = 1/x
        return inner(x, n)
    