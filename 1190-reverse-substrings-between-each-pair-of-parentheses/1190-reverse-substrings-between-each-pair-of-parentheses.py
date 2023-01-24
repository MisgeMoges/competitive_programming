class Solution:
    def reverseParentheses(self, s: str) -> str:
        
            stack = []
            newStr = ""
            for ch in s:
                if ch != ")":
                    stack.append(ch)
                else:
                    newStr = ""
                    while stack[-1] != "(":
                        newStr += stack.pop()

                    stack.pop()
                    for ch in newStr:
                        stack.append(ch)
            return ''.join(stack)

          
         