class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        res = ""
        for bit in binary:
            if bit == "1":
                 res  += "0"
            else:
                res += "1"
        
        return int(res, 2)