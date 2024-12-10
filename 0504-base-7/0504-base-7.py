class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        is_negative = num < 0
        num = abs(num)
        base_seven = []
        
        while num > 0:
            base_seven.append(str(num%7))
            num //= 7
        base_seven_val = ''.join(reversed(base_seven))
        return "-"+base_seven_val if is_negative else base_seven_val
        