class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            # Add digits and carry
            total = digit1 + digit2 + carry
            result.append(str(total % 10))  # Append the single digit to result
            carry = total // 10  # Update the carry

            # Move to the next digits
            i -= 1
            j -= 1

        # The result list is in reverse order, reverse it and join
        return ''.join(reversed(result))

        
        # num1 = num1[::-1]
        # num2 =num2[::-1]
        # if len(num1)<len(num2):
        #     num1 += "0"*(len(num2)-len(num1))
        # else:
        #     num2 += "0"*(len(num1)-len(num2))
        # result = ""
        # carry = 0
        # for i in range(len(num1)):
        #     digit_sum = int(num1[i])+int(num2[i])+carry
        #     carry = digit_sum//10
        #     result += str(digit_sum%10)
        # if carry>0:
        #     result += str(carry)
        # return result[::-1]