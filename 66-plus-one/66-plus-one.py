class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
     
        return list(map(int, list(str(1+int("".join(list(map(str, digits))))))))
#         carry = 1
#         n = len(digits)
#         dig = digits[0]
#         for i in range(n-1, -1, -1):
#             dig = digits[i]
#             if(dig == 9 and carry == 1):
#                 dig = 0
#                 carry = 1
#             else:
#                 dig = dig + carry
#                 carry = 0
#             digits[i] = dig

#         if(carry == 1):
#             extra = [1]
#             digits = extra + digits

#         return digits
	
    
        