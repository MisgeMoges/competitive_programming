class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1
            
        return True
        