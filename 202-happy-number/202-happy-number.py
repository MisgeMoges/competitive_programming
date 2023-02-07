class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            n = sum([int(char)**2 for char in list(str(n))])
        
        return n == 1
